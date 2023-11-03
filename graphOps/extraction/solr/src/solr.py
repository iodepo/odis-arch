import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)  ## remove pandas future warning
import pandas as pd
import geopandas as gpd
from shapely import wkt
# import s3fs
import pyarrow.parquet as pq
import shapely
import requests
import os
import re
import json, io
from pyld import jsonld
import kglab
from minio import Minio
import rdflib
from rdflib import ConjunctiveGraph  #  needed for nquads
from urllib.request import urlopen
from dateutil import parser
import numpy as np
import geopandas as gpd
from shapely.geometry import Point
from pyproj import Geod

# Check for using GPU, in case you want to ensure your GPU is used
# gc = kglab.get_gpu_count()
# print(gc)

"""## Definitions"""

# pop out last element in a quad to make a triple
def popper(input):
    lines = input.decode().split('\n') # Split input into separate lines
    modified_lines = []

    for line in lines:
        newline = line.replace("http://schema.org", "https://schema.org")
        segments = newline.split(' ')

        if len(segments) > 3:
            segments.pop()   # Remove the last two segment
            segments.pop()
            new_line = ' '.join(segments) + ' .'
            modified_lines.append(new_line)

    result_string = '\n'.join(modified_lines)

    return(result_string)

def contextAlignment(input):
    lines = input.decode().split('\n') # Split input into separate lines
    modified_lines = []

    for line in lines:
        newline = line.replace("http://schema.org", "https://schema.org")

        modified_lines.append(newline)

    result_string = '\n'.join(modified_lines)

    return(result_string)

def publicurls(client, bucket, prefix):
    urls = []
    objects = client.list_objects(bucket, prefix=prefix, recursive=True)
    for obj in objects:
        result = client.stat_object(bucket, obj.object_name)

        if result.size > 0:  #  how to tell if an objet   obj.is_public  ?????
            url = client.presigned_get_object(bucket, obj.object_name)
            # print(f"Public URL for object: {url}")
            urls.append(url)

    return urls

def to_wkt(polygon_string):
    # split the input string into pairs
    pairs = polygon_string.split(',')

    # transform each pair into 'y x' format
    # transformed_pairs = [' '.join(reversed(pair.split())) for pair in pairs]
    transformed_pairs = [' '.join(pair.split()) for pair in pairs]


    # join the transformed pairs with a comma and a space
    transformed_string = ', '.join(transformed_pairs)

    # return the final WKT string
    return f"POLYGON (({transformed_string}))"

def contains_alpha(s):
    if isinstance(s, (int, float)):
      return False
    return any(c.isalpha() for c in s)

"""
## Load Graph(s)

At this point we have the URLs, and we could either loop load all of them or pull one out manually and use.  This section dmonstrates loading and working with one
"""

client = Minio("ossapi.oceaninfohub.org:80",  secure=False) # Create client with anonymous access.
urls = publicurls(client, "public", "graph")
# for u in urls:
#   print(u)

# load single quad graph into a RDFLIB conjunctive graph

u = "http://ossapi.oceaninfohub.org/public/graphs/summonedcioos_v1_release.nq"

df = urlopen(u)
dg = df.read()
r = contextAlignment(dg)

g = ConjunctiveGraph()
g.parse(data=r, format="nquads")
print(len(g))

# # load all graphs

# g = ConjunctiveGraph()
# for u in urls:
#   print("loading: {}".format(u))

#   df = urlopen(u)
#   dg = df.read()
#   r = contextAlignment(dg)

#   g.parse(data=r, format="nquads")

# print(len(g))

## Convert the RDFLIB graph to a kglabs graph

namespaces = {
    "sh":   "http://www.w3.org/ns/shacl#" ,
    "schema":   "https://schema.org/" ,
    "schemawrong": "http://schema.org/",
    "geo":      "http://www.opengis.net/ont/geosparql#",
}

kg = kglab.KnowledgeGraph(name = "OIH test", base_uri = "https://oceaninfohub.org/id/", namespaces = namespaces, use_gpus=True, import_graph = g)

"""## Query Section"""

# List of URLs
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
        else:
            print(f"Failed to download URL {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")



qlist = [datasetrq,  sup_georq, sup_temporalrq]

# m1 = pd.merge(pdf, geodf, on='id', how='outer')
# mf = pd.DataFrame()
dfl = []
for q in qlist:
  df = kg.query_as_df(q)
  dfl.append(df)

common_column = ["id", "type"]  # Replace with the actual common column name

# Initialize a merged DataFrame with the first DataFrame
merged_df = dfl[0]

# Iterate through the remaining DataFrames and merge them into the merged_df
for df in dfl[1:]:
    merged_df = pd.merge(merged_df, df, on=common_column, how='inner')

merged_df['id'].nunique()

merged_df.info()

"""## Post processing

### GeoSpatial
"""

merged_df['filteredgeom'] = merged_df['geom'].apply(lambda x: np.nan if contains_alpha(x) else x)

"""### Regions
Incorporate Jeff's regions.py which needs

* address (Org, person, Course?
* name (THING, in all)
* spatialFeature (WKT geom column)
* countryOfLastProcessing (vehicle only)
"""



"""### Temporal"""

merged_df['temporalCoverage'] = merged_df['temporalCoverage'].astype('str')  # fine to make str since we don't use in the solr JSON
merged_df['dt_startDate'] = merged_df['temporalCoverage'].apply(lambda x: re.split("/", x)[0] if "/" in x else np.nan)
merged_df['dt_endDate'] = merged_df['temporalCoverage'].apply(lambda x: re.split("/", x)[1] if "/" in x else np.nan)
merged_df['n_startYear'] = merged_df['dt_startDate'].apply(lambda x: parser.parse(x).year if "-" in str(x) else np.nan)
merged_df['n_endYear'] = merged_df['dt_endDate'].apply(lambda x: parser.parse(x).year if "-" in str(x) else np.nan)

merged_df.info()

merged_df.head()

# transforms needed for aggregation
merged_df['keywords'] = merged_df['keywords'].astype(str)  #  why is this needed?

mf = merged_df.groupby('id').agg({'keywords': ', '.join,
                                        'type': 'first',
                                        'name': ', '.join,
                                        'description': ', '.join,
                                        'url': ', '.join,
                                        'geotype':'first',
                                        'geompred':'first',
                                        'geom':'first',
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

mf.info()

"""## Outpt JSON for Solr

Example Records

https://github.com/iodepo/odis-arch/blob/master/graphOps/extraction/solr/solrexample.json

for

https://catalogue.cioos.ca/dataset/ff0232d8-34bd-4456-be28-20d4f8b2937c.jsonld



"""

# mf.to_parquet('solr_set.parquet')
mf.to_csv('solr_set.csv')
