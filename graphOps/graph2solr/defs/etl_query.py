from io import StringIO
from pathlib import Path

import lancedb
import polars as pl
import requests


def query_mode(source, sink, query, table):
    """Handle query mode operations"""
    print(f"Query mode: Processing data from {source} to {sink}")
    # Add query-specific logic here

    # Need to pass in (minimum): URL, SPARQL file, output table name

    url = source
    params = {
        "timeout": "600s",
        "access-token": "odis_7643543846_6dMISzlPrD7i"
    }
    headers = {
        "Accept": "text/csv",
        "Content-type": "application/sparql-query"
    }

    # Read the SPARQL query from file
    with open(query, "r") as file:
        query = file.read()

    # Send the request
    response = requests.post(url, params=params, headers=headers, data=query)

    # Load response into Polars DataFrame
    df = pl.read_csv(StringIO(response.text))

    print(len(df))


    ## TEMPORAL  ---------------------------------------------------
    # TODO move to augmentation?

    # Method 2: Using pattern matching with coalesce (recommended)
    df = df.with_columns(
        pl.when(
            pl.col("datePublished").str.strptime(pl.Datetime, format="%Y-%m-%d", strict=False).is_not_null()
        )
        .then(pl.col("datePublished").str.strptime(pl.Datetime, format="%Y-%m-%d", strict=False))
        .otherwise(None)
        .alias("datePublished")
    )

    # Then convert back to string in your desired format
    df = df.with_columns(
        pl.when(pl.col("datePublished").is_not_null())
        .then(pl.col("datePublished").dt.strftime("%Y-%m-%d"))  # or any format you want
        .otherwise(None)
        .alias("datePublished")
    )

    df = df.with_columns(
        pl.when(
            pl.col("dateModified").str.strptime(pl.Datetime, format="%Y-%m-%d", strict=False).is_not_null()
        )
        .then(pl.col("dateModified").str.strptime(pl.Datetime, format="%Y-%m-%d", strict=False))
        .otherwise(None)
        .alias("dateModified")
    )

    # Then convert back to string in your desired format
    df = df.with_columns(
        pl.when(pl.col("dateModified").is_not_null())
        .then(pl.col("dateModified").dt.strftime("%Y-%m-%d"))  # or any format you want
        .otherwise(None)
        .alias("dateModified")
    )


    # OLD DATE TIME replaced with code above (delete if fine with the above)
    # ## Temporal alignment ##
    # # Convert the column to ISO datetime format
    # df = df.with_columns(
    #     pl.col("datePublished").str.strptime(pl.Datetime, format="%Y-%m-%d", strict=False).alias("datePublished")
    # )
    #
    # df = df.with_columns(
    #     pl.col("dateModified").str.strptime(pl.Datetime, format="%Y-%m-%d", strict=False).alias("dateModified")
    # )

    # Save to CSV
    # print(f"Saving CSV")
    # df.write_csv(sink)

    # Save to parquet
    # TODO:  just check is .csv or .parquet and save accordingly
    file_path = Path(sink)
    new_file_path = file_path.with_suffix(".parquet")
    print("Saving Parquet")
    df.write_parquet(new_file_path)

    # Create or get LanceDB table and write data
    print("Saving Lance")
    db = lancedb.connect("./stores/lancedb")
    db.create_table(table, data=df, mode="overwrite")
