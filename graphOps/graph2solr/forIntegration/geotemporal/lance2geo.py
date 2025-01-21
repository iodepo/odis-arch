import lancedb
import json
import numpy as np
import polars as pl
# from polars import Series

# from defs import graphshapers
# from defs import load_queries
# from defs import readSource
# from defs import regionFor
# from defs import saveobject
from defs import spatial

# REFERENCS
# in sqlOps:   duckops_wis2.py
# in extraction/mdp   mdp_deprecated.py for temportal and geo conversion

# Example function that processes batches efficiently
# def process_geometry_batch(batch: pl.Series) -> pl.Series:
#     numpy_array = batch.to_numpy()  # Convert to numpy for vectorized operations if needed
#     results = np.array([spatial.gj(str(x), "area") for x in numpy_array])  # Process the entire batch at once
#     return pl.Series(results)

# Connect to LanceDB and generate polars DataFrame
db = lancedb.connect("../../stores/lancedb")
table = db.open_table("sparql_results")
df = pl.from_arrow(table.to_arrow())

print(f"Converted {len(df)} records to a dataframe format")
print(df.schema)

## process geometry  ##

# Convert the column to a NumPy array
filteredgeom_array = df["geom"].to_numpy()

flt_terms = ["area",  "length"]
for term in flt_terms:
    print(f"Processing {term}")
    # Process the data using spatial.gj with error handling
    geoprocess_array = np.array([
        spatial.gj(str(x), term) if x is not None else np.nan
        for x in filteredgeom_array
    ], dtype=np.float64)

    # Ensure the array length matches the DataFrame length and add back in
    if len(geoprocess_array) != len(df):
        raise ValueError(f"Length mismatch: {term} does not match DataFrame length")

    df = df.with_columns(
        pl.Series(term, geoprocess_array)
    )


str_terms = [ "centroid",  "wkt", "geojson"]
for term in str_terms:
    print(f"Processing {term}")
    # Process the data using spatial.gj with error handling
    geoprocess_array = np.array([
        spatial.gj(str(x), term) if x is not None else np.nan
        for x in filteredgeom_array
    ], dtype=np.str_)

    # Ensure the array length matches the DataFrame length and add back in
    if len(geoprocess_array) != len(df):
        raise ValueError(f"Length mismatch: {term} does not match DataFrame length")

    df = df.with_columns(
        pl.Series(term, geoprocess_array)
    )

## process date ##

# # Convert the column to ISO datetime format
# df = df.with_columns(
#     pl.col("datePublished").str.strptime(pl.Datetime, format="%Y-%m-%d", strict=False).alias("datePublished")
# )
#
# df = df.with_columns(
#     pl.col("dateModified").str.strptime(pl.Datetime, format="%Y-%m-%d", strict=False).alias("dateModified")
# )


print(df.dtypes)

df.write_csv("output.csv")

print("End of Line")
