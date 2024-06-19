import argparse
import datetime
import sys
from io import BytesIO
import pandas as pd
import s3fs
import os
import numpy as np

from defs import spatial
from defs import graphshapers

def main():
    # Params
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

    u = args.source
    o = args.output

    # Load graph
    print("Parquet loading", datetime.datetime.now())
    # LOAD PARQUET TO Pandas
    endpoint = 'http://ossapi.oceaninfohub.org'
    access_key = os.getenv('MINIO_ACCESS_KEY')
    secret_key = os.getenv('MINIO_SECRET_KEY')

    fs = s3fs.S3FileSystem(anon=False, client_kwargs={'endpoint_url': endpoint}, key=access_key, secret=secret_key)  # Use 'anon=True' for public data

    with fs.open(u) as f:
        df = pd.read_parquet(f)

    #process the dataframe
    print("Processing Stage: Geospatial centroid")

    df['filteredgeom'] = df['geom'].apply(lambda x: np.nan if graphshapers.contains_alpha(x) else x)

    print("Processing Stage: Geospatial centroid")
    df['centroid'] = df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "centroid"))

    print("Processing Stage: Geospatial length")
    df['length'] = df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "length"))

    print("Processing Stage: Geospatial area")
    df['area'] = df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "area"))

    print("Processing Stage: Geospatial wkt")
    df['wkt'] = df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "wkt"))

    print("Processing Stage: Geospatial geojson")
    df['geojson'] = df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "geojson"))

    print(df.head())

    # Save
    # buf = BytesIO()
    # df.to_parquet(buf)
    #
    # obj = s3.Object(bucket_name=bucket, key='new_' + key)
    # obj.put(Body=buf.getvalue())

if __name__ == "__main__":
    main()