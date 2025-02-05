import lancedb
import json
import numpy as np
import polars as pl
# from polars import Series

from defs import graphshapers
# from defs import load_queries
# from defs import readSource
# from defs import regionFor
# from defs import saveobject
from defs import spatial

# REFERENCS
# in sqlOps:   duckops_wis2.py
# in extraction/mdp   mdp_deprecated.py for temportal and geo conversion

# Connect to LanceDB
db = lancedb.connect("../../stores/lancedb")
table = db.open_table("sparql_results")

# Convert to DataFrame and then to JSONL
df = table.to_pandas()
print(f"Converted {len(df)} records to pandas format")

# GeoSpatial
print("Processing Stage: Geospatial")

if "geom" in df.columns:
    # df['filteredgeom'] = df['geom'].apply(lambda x: np.nan if graphshapers.contains_alpha(x) else x)
    df['filteredgeom'] = df['geom']

    ## Geometry representations

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

else:
    print("NOTE: no geometry data found")

# df['area'] = df['geom'].apply(lambda x: spatial.gj(str(x), "area"))

df.to_csv('geospatial.csv', index=False)

# Create or get LanceDB table and write data
# table = db.create_table(f"{source}_geo", data=df, mode="overwrite")
# print(table)

print("End of Line")
