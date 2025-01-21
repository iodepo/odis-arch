import lancedb
import numpy as np
import pandas as pd
import polars as pl

from defs import graphshapers
from defs import regionFor
from defs import spatial


def augment_mode(source):
    print(f"Augment mode: Processing data from lancedb table {source} to a file")

    # source = "sparql_results_grouped"
    dblocation = "./stores/lancedb"
    table_name = source

    # Connect to LanceDB
    db = lancedb.connect(dblocation)
    table = db[table_name]

    df = pl.from_arrow(table.to_arrow())

    ## SPATIAL Geometry section --------------------------------------------------------------------------------

    # Convert the column to a NumPy array
    filteredgeom_array = df["txt_geom"].to_numpy()

    bool_terms = ["has_geom"]
    for term in bool_terms:
        print(f"Processing {term}")
        # Process the data using spatial.gj with error handling
        has_geom_values = ['true' if not pd.isna(x) else 'false' for x in filteredgeom_array]

        # Ensure the array length matches the DataFrame length and add back in
        if len(has_geom_values) != len(df):
            raise ValueError(f"Length mismatch: {term} does not match DataFrame length")

        df = df.with_columns(
            pl.Series(term, has_geom_values)
        )

    flt_terms = ["area", "length"]
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

    str_terms = ["centroid", "wkt", "geojson"]
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
            pl.Series(term, geoprocess_array)  ## TODO needs to know the ID and Type it came in with!
        )

    ## REGION code -----------------------------------------------------------------------------------------

    # Assuming df is already a Polars DataFrame
    # Define a function to handle None/null values and convert lists to strings
    def safe_region_for_name(x):
        if x is None:
            return []
        result = regionFor.name(x)
        if result is None or (isinstance(result, (list, tuple)) and len(result) == 0):
            return []
        return result

    def safe_region_for_address(x):
        if x is None:
            return []
        result = regionFor.address(x)
        if result is None or (isinstance(result, (list, tuple)) and len(result) == 0):
            return []
        return result

    def safe_region_for_country(x):
        if x is None:
            return []
        result = regionFor.countryLastProcessing(x)
        if result is None or (isinstance(result, (list, tuple)) and len(result) == 0):
            return []
        return result

    def safe_region_for_feature(x):
        if x is None:
            return []
        result = regionFor.feature(x)
        if result is None or (isinstance(result, (list, tuple)) and len(result) == 0):
            return []
        return result

    # Process each column conditionally
    if "name" in df.columns:
        print("Processing region for name")
        df = df.with_columns(
            nregion=pl.col("name").map_elements(safe_region_for_name, return_dtype=pl.List(pl.String))
            # TODO rename back to nregion then join all the arrays in the various columns
        )

    if "address" in df.columns:
        print("Processing region for address")
        df = df.with_columns(
            aregion=pl.col("address").map_elements(safe_region_for_address, return_dtype=pl.List(pl.String))
        )

    if "addressCountry" in df.columns:
        print("Processing region for addressCountry")
        df = df.with_columns(
            cregion=pl.col("addressCountry").map_elements(safe_region_for_country, return_dtype=pl.List(pl.String))
        )

    if "wkt" in df.columns:
        print("Processing region for wkt")
        df = df.with_columns(
            fregion=pl.col("wkt").map_elements(safe_region_for_feature, return_dtype=pl.List(pl.String))
        )

    def combine_regions(row):
        all_regions = set()

        # List of possible region columns
        region_cols = ['nregion', 'aregion', 'cregion', 'fregion']

        for col in region_cols:
            # Check if a column exists in the DataFrame and the value isn't None
            if col in row.keys() and row[col] is not None:
                # As row[col] is now directly a list, just add the elements into the set
                all_regions.update(row[col])

        # print(all_regions)
        # print(list(all_regions) if all_regions else [])
        return list(all_regions) if all_regions else []

    # Add the combined regions column
    print("Combining regions")
    df = df.with_columns(
        txt_regions=pl.struct(df.columns).map_elements(combine_regions, return_dtype=pl.List(pl.String))
    )

    # df = df.with_columns(
    #     txt_regions=df.map_elements(combine_regions, return_dtype=pl.List(pl.String))
    # )

    ## IO section -----------------------------------------------------------------------------------------

    print("Saving Parquet")
    df.write_parquet("./stores/test_augmented.parquet")

    print("Saving Lance")
    db.create_table(f"{source}_augmented", data=df, mode="overwrite")

    # process region ##

    # TO ADD
    #
    #     if "name" in df.columns:
    #         df['name'] = df['name'].astype(str)  # why is this needed?
    #
    #         # TODO, incorporate Jeff's code as a Lambda function (will need to support multiple possible regions per entry)
    #     if "name" in df.columns:
    #         print("Processing region for name")
    #         df['nregion'] = df['name'].apply(lambda x: regionFor.name(x) if x else x)
    #     if "address" in df.columns:
    #         print("Processing region for address")
    #         df['aregion'] = df['address'].apply(lambda x: regionFor.address(x) if x else x)
    #     if "addressCountry" in df.columns:
    #         print("Processing region for addressCountry")
    #         df['cregion'] = df['addressCountry'].apply(
    #             lambda x: regionFor.countryLastProcessing(x) if x else x)
    #     if "wkt" in df.columns:
    #         print("Processing region for wkt")
    #         df['fregion'] = df['wkt'].apply(lambda x: regionFor.feature(x) if x else x)

    # ---------------------------------------------------

    def augment_mode_pandas(source):
        print(f"Augment mode: Processing data from lancedb table {source} to a file")

        # source = "sparql_results_grouped"
        dblocation = "./stores/lancedb"
        table_name = source

        # Connect to LanceDB
        db = lancedb.connect(dblocation)
        table = db[table_name]

        df = table.to_pandas()

        # process the dataframe
        print("Processing Stage: Geospatial centroid")

        df['filteredgeom'] = df['txt_geom'].apply(lambda x: np.nan if graphshapers.contains_alpha(x) else x)

        print("Processing Stage: Geospatial centroid")
        df['centroid'] = df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "centroid"))
        df['centroid'] = df['centroid'].astype(str)

        print("Processing Stage: Geospatial length")
        df['length'] = df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "length"))

        print("Processing Stage: Geospatial area")
        df['area'] = df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "area"))

        print("Processing Stage: Geospatial wkt")
        df['wkt'] = df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "wkt"))
        df['wkt'] = df['wkt'].astype(str)

        print("Processing Stage: Geospatial geojson")
        df['geojson'] = df['filteredgeom'].apply(lambda x: spatial.gj(str(x), "geojson"))
        df['geojson'] = df['geojson'].astype(str)

        print(df.head())
