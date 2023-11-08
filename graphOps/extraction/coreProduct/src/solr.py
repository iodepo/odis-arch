import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)  ## remove pandas future warning
import pandas as pd
# import s3fs
import requests
import re
import kglab
from tqdm import tqdm
from rdflib import ConjunctiveGraph  # needed for nquads
from urllib.request import urlopen
from dateutil import parser
import numpy as np

from defs import graphshapers
from defs import readSource


def main():
    # URL for the release graph to process
    u = "http://ossapi.oceaninfohub.org/public/graphs/summonedcioos_v1_release.nq"
    dg = readSource.read_data(u)
    graphProcessor(dg)

def graphProcessor(dg):
    # load single quad graph into a RDFLIB conjunctive graph
    # df = urlopen(u)
    # dg = df.read()

    r = graphshapers.contextAlignment(dg)
    g = ConjunctiveGraph()
    g.parse(data=r, format="nquads")
    print("Number of quads loaded: {}".format(len(g)))

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

    # in many IDEs the vars for qlist will look like an error since these vars are dynamic set at runtime via globals()
    qlist = [datasetrq, sup_georq, sup_temporalrq]

    # m1 = pd.merge(pdf, geodf, on='id', how='outer')  # mf = pd.DataFrame()
    dfl = []
    print(
        "Processing {} SPARQL queries. This will be slow and the progress bar updates only on query completion".format(
            len(qlist)))
    for q in tqdm(qlist):
        df = kg.query_as_df(q)
        dfl.append(df)

    common_column = ["id", "type"]  # Replace with the actual common column name

    # Initialize a merged DataFrame with the first DataFrame
    merged_df = dfl[0]

    # Iterate through the remaining DataFrames and merge them into the merged_df
    for df in dfl[1:]:
        merged_df = pd.merge(merged_df, df, on=common_column, how='inner')

    merged_df['id'].nunique()

    # merged_df.info()

    """## Post processing
    
    ### GeoSpatial
    """

    merged_df['filteredgeom'] = merged_df['geom'].apply(lambda x: np.nan if graphshapers.contains_alpha(x) else x)

    # TODO, incorporate Jeff's code as a Lambda function (will need to support multiple possible regions per entry)
    """### Regions
    Incorporate Jeff's regions.py which needs
    
    * address (Org, person, Course?
    * name (THING, in all)
    * spatialFeature (WKT geom column)
    * countryOfLastProcessing (vehicle only)
    """

    # Temporal shaping
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

    # transforms needed for aggregation
    merged_df['keywords'] = merged_df['keywords'].astype(str)  # why is this needed?

    mf = merged_df.groupby('id').agg({'keywords': ', '.join,
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
                                      'dt_startDate': 'first',
                                      'dt_endDate': 'first',
                                      'n_startYear': 'first',
                                      'n_endYear': 'first'}).reset_index()

    print("Combined dataframe information")
    print(mf.info())

    print("Saving results to file")
    # Output the results to a file, eith or both of parquet or csv
    mf.to_parquet('solr_set.parquet')
    # mf.to_csv('solr_set.csv')

if __name__ == '__main__':
    main()
