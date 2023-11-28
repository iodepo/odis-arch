import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)  ## remove pandas future warning
import pandas as pd
import requests
import re
import kglab
from tqdm import tqdm
from rdflib import ConjunctiveGraph  # needed for nquads
from dateutil import parser
import numpy as np
import argparse
import sys
import os
# import s3fs

from defs import graphshapers
from defs import readSource
from defs import spatial
from defs import regionFor

def main():
    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument("--source", type=str, help="Source URL")
    parser.add_argument("--output", type=str, help="Output file")

    args = parser.parse_args()

    if args.source is None:
        print("Error: the --source argument is required")
        sys.exit(1)

    if args.output is None:
        print("Error: the --output argument is required")
        sys.exit(1)

    # URL for the release graph to process
    u = args.source
    output_file = args.output

    dg = readSource.read_data(u)
    mf = graphProcessor(dg)

    ### Save
    print("Reporting Stage: The following is the current dataframe shape to exported")
    print(mf.info())

    print("Saving results to file")
    _, file_extension = os.path.splitext(output_file)

    ## TODO why is this here?  likely should be down in the geo section
    mf['centroid'] = mf['centroid'].astype(str)

    if file_extension == '.parquet':
        mf.to_parquet(output_file, engine='fastparquet')  # engine must be one of 'pyarrow', 'fastparquet'
    elif file_extension == '.csv':
        mf.to_csv(output_file)
    else:
        print(f'Error: unsupported file extension {file_extension}. Support .parquet or .csv only')
        sys.exit(1)


def graphProcessor(dg):
    # load single quad graph into a RDFLIB conjunctive graph
    # df = urlopen(u)
    # dg = df.read()

    r = graphshapers.contextAlignment(dg)
    g = ConjunctiveGraph()
    g.parse(data=r, format="nquads")
    print("Number of quads loaded: {}".format(len(g)))

    # This code is no longer used but, I am keeping in case I want to build a looping set ever
    # # load all graphs
    # client = Minio("ossapi.oceaninfohub.org:80",  secure=False) # Create client with anonymous access.
    # urls = graphshapers.publicurls(client, "public", "graph")
    # g = ConjunctiveGraph()
    # for u in urls:
    #   print("loading: {}".format(u))
    #   df = urlopen(u)
    #   dg = df.read()
    #   r = contextAlignment(dg)
    #   g.parse(data=r, format="nquads")
    # print(len(g))

    # Convert the RDFLIB graph to a kglabs graph
    namespaces = {
        "sh": "http://www.w3.org/ns/shacl#",
        "schema": "https://schema.org/",
        "schemawrong": "http://schema.org/",
        "geo": "http://www.opengis.net/ont/geosparql#",
    }

    kg = kglab.KnowledgeGraph(name="OIH test", base_uri="https://oceaninfohub.org/id/", namespaces=namespaces,
                              use_gpus=True, import_graph=g)

    # Load Query Section, queries are loading via the net from GitHub URLs
    urls = [
        "https://raw.githubusercontent.com/iodepo/odis-in/master/SPARQL/searchOIH/sup_geo.rq",
        "https://raw.githubusercontent.com/iodepo/odis-in/master/SPARQL/searchOIH/sup_temporal.rq",
        "https://raw.githubusercontent.com/iodepo/odis-in/master/SPARQL/searchOIH/dataset.rq"
    ]

    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                # Extract the file name from the URL and change ".rq" to "rq"
                file_name = url.split("/")[-1].replace(".rq", "rq")
                content = response.text

                # Create a variable with the modified name and store the content
                globals()[file_name] = content
                print(f"Loaded SPARQL from URL {url}. Status code: {response.status_code}")
            else:
                print(f"Failed to download URL {url}. Status code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    # NOTE: In many IDEs the vars for qlist will look like an error since these vars are dynamic set at runtime via globals()
    qlist = [datasetrq, sup_georq, sup_temporalrq]

    # m1 = pd.merge(pdf, geodf, on='id', how='outer')  # mf = pd.DataFrame()
    dfl = []
    print(
        "Processing {} SPARQL queries. This will be slow and the progress bar updates only on query completion".format(
            len(qlist)))
    for q in tqdm(qlist):
        df = kg.query_as_df(q)
        if len(df) > 0:  # don't append in empty result sets, breaks the merge
            dfl.append(df)

    common_column = ["id", "type"]  # Replace with the actual common column name

    # Initialize a merged DataFrame with the first DataFrame
    merged_df = dfl[0]

    # Iterate through the remaining DataFrames and merge them into the merged_df
    for df in dfl[1:]:
        merged_df = pd.merge(merged_df, df, on=common_column, how='inner')

    merged_df['id'].nunique()

    # merged_df.info()

    ### GeoSpatial
    print("Processing Stage: Geospatial")

    merged_df['filteredgeom'] = merged_df['geom'].apply(lambda x: np.nan if graphshapers.contains_alpha(x) else x)

    ## Geometry representations

    print("Processing Stage: Geospatial centroid")
    merged_df['centroid'] = merged_df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "centroid"))

    print("Processing Stage: Geospatial length")
    merged_df['length'] = merged_df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "length"))

    print("Processing Stage: Geospatial area")
    merged_df['area'] = merged_df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "area"))

    print("Processing Stage: Geospatial wkt")
    merged_df['wkt'] = merged_df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "wkt"))

    print("Processing Stage: Geospatial geojson")
    merged_df['geojson'] = merged_df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "geojson"))

    # TODO, incorporate Jeff's code as a Lambda function (will need to support multiple possible regions per entry)
    merged_df['nregion'] = merged_df['name'].apply(lambda x: regionFor.name(x) if x else x)
    merged_df['aregion'] = merged_df['address'].apply(lambda x: regionFor.address(x) if x else x)
    merged_df['cregion'] = merged_df['addressCountry'].apply(lambda x: regionFor.countryLastProcessing(x) if x else x)
    merged_df['fregion'] = merged_df['wkt'].apply(lambda x: regionFor.feature(x) if x else x)

    merged_df = regionFor.mergeRegions(merged_df.copy())

    ### Temporal shaping
    print("Processing Stage: Temporal")

    merged_df['temporalCoverage'] = merged_df['temporalCoverage'].astype(
        'str')  # fine to make str since we don't use in the solr JSON
    merged_df['dt_startDate'] = merged_df['temporalCoverage'].apply(
        lambda x: re.split("/", x)[0] if "/" in x else np.nan)
    merged_df['dt_endDate'] = merged_df['temporalCoverage'].apply(lambda x: re.split("/", x)[1] if "/" in x else np.nan)
    merged_df['n_startYear'] = merged_df['dt_startDate'].apply(
        lambda x: parser.parse(x).year if "-" in str(x) else np.nan)
    merged_df['n_endYear'] = merged_df['dt_endDate'].apply(lambda x: parser.parse(x).year if "-" in str(x) else np.nan)

    # Check frames after temporal ETL calls
    # merged_df.info()
    # merged_df.head()

    ### Dataframe groupby, aggregation and joins
    print("Processing Stage: Dataframe shaping")

    # transforms needed for aggregation
    merged_df['keywords'] = merged_df['keywords'].astype(str)  # why is this needed?
    merged_df['geom'] = merged_df['geom'].astype(str)  # why is this needed?
    merged_df['filteredgeom'] = merged_df['filteredgeom'].astype(str)  # why is this needed?
    merged_df['centroid'] = merged_df['centroid'].astype(str)  # why is this needed?

    agg_dict = {'keywords': ', '.join,
                'type': 'first',
                'name': ', '.join,
                'description': ', '.join,
                'url': ', '.join,
                'geotype': 'first',
                'geompred': 'first',
                'geom': 'first',
                'temporalCoverage': 'first',
                'datePublished': 'first',
                'license': 'first',
                'creator': 'first',
                'includedInDataCatalog': 'first',
                'distribution': 'first',
                'publisher': 'first',
                'filteredgeom': 'first',
                'region': 'first',
                'dt_startDate': 'first',
                'dt_endDate': 'first',
                'n_startYear': 'first',
                'n_endYear': 'first',
                'centroid': 'first',
                'length': 'first',
                'area': 'first',
                'wkt': 'first',
                'geojson': 'first'}

    for col in agg_dict.copy():
        if col not in merged_df.columns:
            del agg_dict[col]

    mf = merged_df.groupby('id').agg(agg_dict).reset_index()

    return mf

if __name__ == '__main__':
    main()
