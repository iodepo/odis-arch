import lancedb
import pandas as pd
from h3converter import h3converter
import geopandas as gpd
from shapely.geometry import Polygon, MultiPolygon, shape, mapping
from shapely import wkt
import json

def geom2h3_mode(source):
    print(f"geom2h3 mode: Processing data from lancedb table {source} to a file")

    dblocation = "../stores/lancedb"
    table_name = source

    # Connect to LanceDB
    db = lancedb.connect(dblocation)
    table = db[table_name]

    df = table.to_pandas()

    # drop all rows where value is nan or None
    # df['geojson'].replace(['None', 'NaN', 'nan'], [None, None, None], inplace=True)
    # df.dropna(subset=['geojson'], inplace=True)

    # remove all but polygons for now to test path
    df.drop(df[~df['geojson'].str.contains("POLYGON", case=False)].index, inplace=True)
    df['geometry'] = df['wkt'].apply(wkt.loads)
    df['geojson_shapely'] = df['geometry'].apply(lambda geometry: mapping(geometry))   # shapely.mapping, need a trap for any potential failed results?

    def process_geojson(x):
        try:
            s = h3converter.polyfill(x, 5)
            return s
        except Exception as e:
            print(f"Encountered an error: {e}")
            print(f"Input GeoJSON: {x}")
            # print(f"Shapely GeoJSON: {shapely_geom}")
            return None


    df['h3_cells'] = df['geojson_shapely'].apply(lambda x: process_geojson(x) if x is not None else None)

    df.dropna(subset=['h3_cells'], inplace=True)

    df['h3_cells'] = df['h3_cells'].apply(lambda x: ','.join(x) if x is not None else None)

    hdf = gpd.read_parquet("/home/fils/scratch/data/hexagonGlobalGrids/hexagons5.parquet")  # 14,117,882 entries

    count_dict = {}
    for cell in df['h3_cells']:
        for item in cell:
            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1

    # Creating a new DataFrame from the dictionary
    cellcounts_df = pd.DataFrame(list(count_dict.items()), columns=['Hexagon_ID', 'Count'])
    merged_df = hdf.merge(cellcounts_df, on='Hexagon_ID', how='inner')

    df.to_parquet('h3.parquet', compression='gzip')

    print(f"Calculated h3 grids for table {table_name}")


def main():
    geom2h3_mode("sparql_results_grouped_augmented")

if __name__ == "__main__":
    main()

