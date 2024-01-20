import argparse
import os, io
import sys
import numpy as np
import pandas as pd
from objdict import ObjDict
import boto3
import pyarrow.parquet as pq
import s3fs

from defs import readobject

# Master Data Product to Solr

def main():
    parser = argparse.ArgumentParser(description="Process arguments")
    parser.add_argument("--source", type=str, help="Source file/URL")
    parser.add_argument("--outputdir", type=str, help="Output directory")

    args = parser.parse_args()

    if args.source is None:
        print("Error: the --source argument is required")
        sys.exit(1)

    if args.outputdir is None:
        print("Error: the --outputdir argument is required")
        sys.exit(1)

    u = args.source
    od = args.outputdir

    _, file_extension = os.path.splitext(u)
    if file_extension != '.parquet':
        print(f'Error: unsupported file extension {file_extension}. Support .parquet only at this time')
        sys.exit(1)

    # Set output directory and make it if it is not present
    if not os.path.exists(od):
        os.makedirs(od)

    # Load the master data product from ODIS
    # mf = pd.read_parquet(u)
    b =  readobject.getBytes(u)
    table = pq.read_table(io.BytesIO(b))

    # Convert to pandas dataframe
    mf = table.to_pandas()

    for index, row in mf.iterrows():
        data = ObjDict()

        # not in arrays
        if "id" in mf.columns:
            data.id = remove_brackets(row['id'])
        if "type" in mf.columns:
            data.type = row['type']

        if "keywords" in mf.columns:
            if not isinstance(row['keywords'], (int, float)):
                data.txt_keywords = [x.strip() for x in row['keywords'].split(',')]

        if "name" in mf.columns:
            if not isinstance(row['name'], (int, float)):
                data.txt_name = row['name']

        if "description" in mf.columns:
            data.description = row['description']
        if "url" in mf.columns:
            data.txt_url = [row['url']]
        if "license" in mf.columns:
            data.txt_license = [row['license']]
        if "creator" in mf.columns:
            data.txt_creator = [row['creator']]

        if "includedInDataCatalog" in mf.columns:
            data.txt_includedInDataCatalog = [remove_brackets(row['includedInDataCatalog'])]

        if "distribution" in mf.columns:
            data.txt_distribution = [row['distribution']]

        if "publisher" in mf.columns:
            data.txt_publisher = [remove_brackets(row['publisher'])]

        # geo
        if "filteredgeom" in mf.columns:
            if row["filteredgeom"] != np.nan:
                data.geom = [row["filteredgeom"]]
                data.geotype = [row['geompred']]
        if "centroid" in mf.columns:
            data.geojson_point = [row["centroid"]]
        if "length" in mf.columns:
            data.geom_length = [row["length"]]
        if "area" in mf.columns:
            data.geom_area = [row["area"]]
        if "geojson" in mf.columns:               ## TODO geojson and geojson_simple are the same for now, resolve
            data.geojson = [row["geojson"]]
            data.geojson_simple = [row["geojson"]]
        if "wkt" in mf.columns:
            data.wkt_geom = [row["wkt"]]

        # temporal
        if "dt_startDate" in mf.columns:
            data.dt_startDate = [row['dt_startDate']]
        if "dt_endDate" in mf.columns:
            data.dt_endDate = [row['dt_endDate']]
        if "n_startYear" in mf.columns:
            data.n_startYear = [row['n_startYear']]
        if "n_endYear" in mf.columns:
            data.n_endYear = [row['n_endYear']]

        # write
        json_string = data.dumps(indent=4)

        # Define the filename based on the row index or a unique identifier from your data
        filename = os.path.join(od, f'row_{index}.json')

        # Write the JSON string to the file
        with open(filename, 'w') as json_file:
            json_file.write(json_string)


def remove_brackets(string):
    if isinstance(string, (int, float)):
        return string
    if string.startswith('<') and string.endswith('>'):
        return string[1:-1]
    else:
        return string

if __name__ == '__main__':
    main()
