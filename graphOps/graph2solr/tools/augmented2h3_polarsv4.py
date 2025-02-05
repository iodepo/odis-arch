import json
import lancedb
import polars as pl
from shapely import wkt
from shapely.geometry import mapping
from typing import Optional, List
from concurrent.futures import ProcessPoolExecutor
from h3converter import h3converter
from tqdm import tqdm


def wkt_to_geojson(wkt_str: str) -> Optional[str]:
    """Convert WKT to GeoJSON"""
    try:
        geometry = wkt.loads(wkt_str)
        return json.dumps(mapping(geometry))
    except Exception as e:
        print(f"Error converting WKT: {e}")
        return None

def wkt_to_geojson_parallel(x: List[str]) -> List[Optional[str]]:
    """Parallel conversion of WKT to GeoJSON using ProcessPoolExecutor"""
    with ProcessPoolExecutor(max_workers=6) as executor:
        results = list(executor.map(wkt_to_geojson, x))
    return results

def process_geojson(geojson):
    if geojson is None:
        return None
    try:
        return ','.join(h3converter.polyfill(json.loads(geojson), 5))
    except Exception as e:
        print(f"Encountered an error: {e}")
        print(f"Input GeoJSON: {geojson}")
        return None

def process_geojson_parallel(x: List[str]) -> List[Optional[str]]:
    """Parallel conversion of WKT to GeoJSON using ProcessPoolExecutor with progress bar"""
    total = len(x)
    with ProcessPoolExecutor(max_workers=9) as executor:
        results = list(tqdm(
                           executor.map(process_geojson, x),
                           total=total,
                           desc="Converting to h3 cells",
                           unit="records"
                       ))
    return results

# def process_geojson_parallel(x: List[str]) -> List[Optional[str]]:
#     """Parallel conversion of WKT to GeoJSON using ProcessPoolExecutor"""
#     with ProcessPoolExecutor(max_workers=12) as executor:
#         results = list(executor.map(process_geojson, x))
#     return results

def geom2h3_mode(source: str) -> pl.DataFrame:
    print(f"geom2h3 mode: Processing data from LanceDB table {source}")

    # Connect to LanceDB
    db = lancedb.connect("../stores/lancedb")
    table = db[source]

    # Convert to Polars DataFrame (eager mode for parallel processing)
    arrow_table = table.to_arrow()
    df = pl.from_arrow(arrow_table)

    print(len(df))

    # Filter rows containing 'polygon' in the 'geojson' column
    filtered_df = df.filter(
        pl.col('geojson').str.to_lowercase().str.contains('polygon')
    )

    # filtered_df = filtered_df.head(500)

    # Extract the 'wkt' column as a list for parallel processing
    wkt_list = filtered_df['wkt'].to_list()

    # Use parallel processing for WKT to GeoJSON conversion
    geojson_shapely_list = wkt_to_geojson_parallel(wkt_list)

    # Add the processed 'geojson_shapely' column back to the DataFrame
    result_df = filtered_df.with_columns(
        pl.Series('geojson_shapely', geojson_shapely_list)
    )

    gj_list = result_df['geojson_shapely'].to_list()

    # Use parallel processing for WKT to GeoJSON conversion
    h3_list = process_geojson_parallel(gj_list)

    # Add the processed 'geojson_shapely' column back to the DataFrame
    # result_df2 = filtered_df.with_columns(
        # pl.Series('h3_cells', h3_list)
    # )

    print(f"Calculated h3 grids for table {source}")
    print(len(result_df2))  # Print the result for debugging or further processing
    return result_df2


def main():
    result = geom2h3_mode("sparql_results_grouped_augmented")
    # Save or process the result as needed
    result.write_parquet("h3.parquet", compression="gzip")
    # result.write_csv("processed_results.csv")


if __name__ == "__main__":
    main()
