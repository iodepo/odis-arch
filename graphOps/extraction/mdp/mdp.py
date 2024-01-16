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
import os, io
import gc
from functools import reduce
import pyarrow as pa
import pyarrow.parquet as pq


# import s3fs

from defs import graphshapers
from defs import readSource
from defs import spatial
from defs import regionFor
from defs import load_queries

from minio import Minio


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

    ### Reporting
    print("Reporting Stage: The following is the current dataframe shape to exported")
    print(mf.info())

    ### Save to file
    print("Saving results to file")
    _, file_extension = os.path.splitext(output_file)

    if file_extension == '.parquet':
        mf.to_parquet(output_file, engine='fastparquet')  # engine must be one of 'pyarrow', 'fastparquet'
    elif file_extension == '.csv':
        mf.to_csv(output_file)
    else:
        print(f'Error: unsupported file extension {file_extension}. Support .parquet or .csv only')
        sys.exit(1)

    ## Save to minio
    print("Saving results to minio")

    sk = os.getenv("MINIO_SECRET_KEY")
    ak = os.getenv("MINIO_ACCESS_KEY")

    # Create client with access and secret key.
    mc = Minio("nas.lan:49153", ak, sk, secure=False)

    bucket_name = 'public'
    object_name =  "graphs/products/{}".format(os.path.basename(output_file))

    # Convert the DataFrame to a parquet file
    table = pa.Table.from_pandas(mf)
    buf = io.BytesIO()
    pq.write_table(table, buf)
    buf.seek(0)

    try:
        mc.put_object(bucket_name, object_name,  buf, len(buf.getvalue()))
    except Exception as e:
        print(f"Error saving object: {e}")


def graphProcessor(dg):
    r = graphshapers.contextAlignment(dg)

    g = ConjunctiveGraph()
    g.parse(data=r, format="nquads")
    print("Number of quads loaded: {}".format(len(g)))


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
    # sl = [
        # "https://raw.githubusercontent.com/iodepo/odis-in/master/SPARQL/searchOIH/baseQuery.rq",
        # "https://raw.githubusercontent.com/iodepo/odis-in/master/SPARQL/searchOIH/sup_geo.rq",
        # "https://raw.githubusercontent.com/iodepo/odis-in/master/SPARQL/searchOIH/sup_temporal.rq",
        # "https://raw.githubusercontent.com/iodepo/odis-in/master/SPARQL/searchOIH/dataset.rq",
        # "https://raw.githubusercontent.com/iodepo/odis-in/master/SPARQL/searchOIH/person.rq"
    # ]

    sfl = [
        "./queries/baseQuery.rq",
        "./queries/sup_geo.rq",
        "./queries/sup_temporal.rq",
        "./queries/dataset.rq",
        "./queries/person.rq"
    ]

    qlist = load_queries.read_files(sfl)

    # Processes the queries now
    dfl = []
    print(
        "Processing {} SPARQL queries. Can be slow, progress bar updates on query completion".format(len(qlist)))
    for q in tqdm(qlist.values()):
        df = kg.query_as_df(q)
        if len(df) > 0:  # don't append in empty result sets, breaks the merge
            # df.info()
            dfl.append(df)

    common_column = ["id", "type"]
    merged_df = reduce(lambda left, right: pd.merge(left, right, on=common_column,suffixes=('_left', '_right'), how='outer'), dfl)

    # Initialize a merged DataFrame with the first DataFrame
    # merged_df = dfl[0]
    #
    # # Iterate through the remaining DataFrames and merge them into the merged_df
    # common_column = "id"    #, "type"]  # Replace with the actual common column name
    # for df in dfl[1:]:
    #     print("Current count : {}".format(merged_df['id'].nunique()))
    #     merged_df = pd.merge(merged_df, df, on=common_column, how='inner')
    #     print("Current count : {}".format(merged_df['id'].nunique()))

    merged_df.info()

    # Hint to the garbage collector that it's cleanup time
    gc.collect()

    ### Temporal shaping
    print("Processing Stage: Temporal")

    if "temporalCoverage" in merged_df.columns:
        merged_df['temporalCoverage'] = merged_df['temporalCoverage'].astype( 'str')  # fine to make str since we don't use in the solr JSON
        merged_df['dt_startDate'] = merged_df['temporalCoverage'].apply( lambda x: re.split("/", x)[0] if "/" in x else np.nan)
        merged_df['dt_endDate'] = merged_df['temporalCoverage'].apply(lambda x: re.split("/", x)[1] if "/" in x else np.nan)
        merged_df['n_startYear'] = merged_df['dt_startDate'].apply( lambda x: parser.parse(x).year if "-" in str(x) else np.nan)
        merged_df['n_endYear'] = merged_df['dt_endDate'].apply(lambda x: parser.parse(x).year if "-" in str(x) else np.nan)
    else:
        print("NOTE:  no temporal data found")

    # EXIT
    # sys.exit(0)

    # Check frames after temporal ETL calls
    # merged_df.info()
    # merged_df.head()

    ### GeoSpatial
    print("Processing Stage: Geospatial")

    if "geom" in merged_df.columns:
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


    else:
        print("NOTE: no geometry data found")


    if "name" in merged_df.columns:
        merged_df['name'] = merged_df['name'].astype(str)  # why is this needed?

    # TODO, incorporate Jeff's code as a Lambda function (will need to support multiple possible regions per entry)
    if "name" in merged_df.columns:
        print("Processing region for name")
        merged_df['nregion'] = merged_df['name'].apply(lambda x: regionFor.name(x) if x else x)
    if "address" in merged_df.columns:
        print("Processing region for address")
        merged_df['aregion'] = merged_df['address'].apply(lambda x: regionFor.address(x) if x else x)
    if "addressCountry" in merged_df.columns:
        print("Processing region for addressCountry")
        merged_df['cregion'] = merged_df['addressCountry'].apply(lambda x: regionFor.countryLastProcessing(x) if x else x)
    if "wkt" in merged_df.columns:
        print("Processing region for wkt")
        merged_df['fregion'] = merged_df['wkt'].apply(lambda x: regionFor.feature(x) if x else x)

    # merged_df = regionFor.mergeRegions(merged_df.copy())

    ### Dataframe groupby, aggregation and joins
    print("Processing Stage: Dataframe shaping")

    if "id" in merged_df.columns:
        merged_df['id'] = merged_df['id'].astype(str)  # why is this needed?
    if "url" in merged_df.columns:
        merged_df['url'] = merged_df['url'].astype(str)  # why is this needed?
    if "description" in merged_df.columns:
        merged_df['description'] = merged_df['description'].astype(str)  # why is this needed?


    # transforms needed for aggregation
    if "keywords" in merged_df.columns:
        merged_df['keywords'] = merged_df['keywords'].astype(str)  # why is this needed?

    if "geom" in merged_df.columns:
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

    print(merged_df.head())

    mf = merged_df.groupby('id').agg(agg_dict).reset_index()

    return mf

if __name__ == '__main__':
    main()
