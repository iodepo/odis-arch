import argparse
import os
import sys

import numpy as np
import pandas as pd
from objdict import ObjDict


# Master Data Product to Solr

def main():
    parser = argparse.ArgumentParser(description="Process some arguments.")
    parser.add_argument("--source", type=str, help="Source URL")
    parser.add_argument("--outputdir", type=str, help="Output directory")

    args = parser.parse_args()

    if args.source is None:
        print("Error: the --source argument is required")
        sys.exit(1)

    if args.outputdir is None:
        print("Error: the --outputdir argument is required")
        sys.exit(1)

    u = args.source
    output_dir = args.outputdir

    _, file_extension = os.path.splitext(u)
    if file_extension != '.parquet':
        print(f'Error: unsupported file extension {file_extension}. Support .parquet only at this time')
        sys.exit(1)

    # Set output directory and make it if it is not present
    output_directory = output_dir
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Load the master data product from ODIS
    mf = pd.read_parquet(u)

    for index, row in mf.iterrows():
        # Create a JSON string from the row
        # json_string = row.to_json()

        data = ObjDict()
        sd = ObjDict()

        # not in arrays
        data.id = remove_brackets(row['id'])
        data.type = row['type']

        if not isinstance(row['keywords'], (int, float)):
            data.txt_keywords = [x.strip() for x in row['keywords'].split(',')]

        if not isinstance(row['name'], (int, float)):
            data.txt_name = row['name']

        data.description = row['description']
        data.txt_url = [row['url']]
        data.txt_license = [row['license']]
        data.txt_creator = [row['creator']]

        #TODO need to add this column check to all the rows
        if "includedInDataCatalog" in mf.columns:
            data.txt_includedInDataCatalog = [remove_brackets(row['includedInDataCatalog'])]

        if "distribution" in mf.columns:
            data.txt_distribution = [row['distribution']]

        data.txt_publisher = [remove_brackets(row['publisher'])]

        # geo
        if row["filteredgeom"] != np.nan:
            data.geotype = [row['geompred']]
            data.geom = [row["filteredgeom"]]

        data.geojson_point = [row["centroid"]]
        data.geojson_simple = [row["geojson"]]
        data.geojson_geom = [row["geojson"]]
        data.geom_area = [row["area"]]
        data.geom_length = [row["length"]]

        # temporal
        data.dt_startDate = [row['dt_startDate']]
        data.dt_endDate = [row['dt_endDate']]
        data.n_startYear = [row['n_startYear']]
        data.n_endYear = [row['n_endYear']]

        # write
        json_string = data.dumps(indent=4)

        # Define the filename based on the row index or a unique identifier from your data
        filename = os.path.join(output_directory, f'row_{index}.json')

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
