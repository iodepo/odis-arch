import datetime
import io
import os
import re
import warnings

import pandas as pd
from minio import Minio
from pyoxigraph import *

from defs import graphshapers
from defs import load_queries
from defs import readSource
from defs import saveobject

warnings.simplefilter(action='ignore', category=FutureWarning)  # remove pandas future warning

def main():
    ak = 'MINIO_ACCESS_KEY'  # Replace ENV_VAR_NAME with your actual environment variable name
    if ak in os.environ:
        akvar = os.environ[ak]
        # print(akvar)
    else:
        print(f'Environment variable {ak} is not set.')

    sk = 'MINIO_SECRET_KEY'  # Replace ENV_VAR_NAME with your actual environment variable name
    if sk in os.environ:
        skvar = os.environ[sk]
        # print(skvar)
    else:
        print(f'Environment variable {sk} is not set.')

    ep="ossapi.oceaninfohub.org"
    bucket = "commons"
    prefix = "ODIS-KG-MAIN/18042024"

    # client = Minio("ossapi.oceaninfohub.org:80", secure=False)  # Create client with anonymous access.
    client = Minio(endpoint=ep, access_key=akvar, secret_key=skvar, secure=False)  # Create client with secure access.

    objects = client.list_objects(
            bucket_name=bucket, prefix=prefix, recursive=True,
    )

    for obj in objects:
        dg = readSource.read_data(f"s3://{ep}/{bucket}/{obj.object_name}")
        graphProcessor(dg, obj.object_name)

def getvalue(x):
  return x.value

# Process the graphs
def graphProcessor(dg, oname):
    print("RDF aligning", datetime.datetime.now())
    r = graphshapers.contextAlignment(dg)

    store = Store()
    mime_type = "application/n-quads"
    store.load(io.StringIO(r), mime_type, base_iri=None, to_graph=None)
    print("RDF querying", datetime.datetime.now())

    # Query sources
    sflFull = [
        "./queries/baseQuery.rq",
        "./queries/course.rq",
        "./queries/dataset.rq",
        "./queries/person.rq",
        "./queries/sup_geo.rq",
        "./queries/sup_temporal.rq"
    ]

    # Query sources
    sfl = [
        "./queries/sup_geo.rq"
    ]

    qlist = load_queries.read_files(sfl)

    for q in sfl:
        match = re.search(r'/([^_/]*)_', oname)  # this doesn't need to be in the loop
        provider_name = match.group(1)

        match2 =  re.search(r'/([^/.]*)\.rq', q)
        query_name = match2.group(1)

        sparql = load_queries.read_file(q)

        sq = store.query(sparql)
        qr = list(sq)

        o = f"s3://ossapi.oceaninfohub.org/commons/OIH-PROD/18042024/{provider_name}_{query_name}.parquet"

        print("Length SPARQL results:  {}".format(len(qr)))

        if len(qr) > 0:
            df = pd.DataFrame(qr)
            df = df.applymap(lambda x: x.value if x is not None else None)

            column_names = list(map(getvalue, sq.variables))
            df.columns = column_names

            dfstr = df.astype(str) # convert all to strings.

            saveobject.write_data(o, dfstr)

if __name__ == '__main__':
    main()
