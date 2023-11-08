import os

import pandas as pd
from objdict import ObjDict


# Master Data Product to Solr

def remove_brackets(string):
    if isinstance(string, (int, float)):
        return string
    if string.startswith('<') and string.endswith('>'):
        return string[1:-1]
    else:
        return string


# Set output directory and make it if it is not present
output_directory = 'output'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Load the master data product from ODIS
mf = pd.read_parquet('solr_set.parquet')

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
    data.txt_includedInDataCatalog = [remove_brackets(row['includedInDataCatalog'])]
    data.txt_distribution = [row['distribution']]
    data.txt_publisher = [remove_brackets(row['publisher'])]

    # # geo
    # if row["filteredgeom"] != np.nan:
    #      data.geotype = [row['geompred']]
    #      data.geom = [ row["filteredgeom"]]
    #  data.geojson_point = [ row["filteredgeom"]]
    #  data.geojson_simple = [ row["filteredgeom"]]
    #  data.geojson_geom = [ row["filteredgeom"]]
    #  data.geom_area = [ row["filteredgeom"]]
    #  data.geom_length = [ row["filteredgeom"]]

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
