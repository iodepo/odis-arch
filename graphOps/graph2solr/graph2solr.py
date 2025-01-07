import argparse
import json
import sys
from io import StringIO
from pathlib import Path
import datetime as dt
import pandas as pd
import duckdb
import lancedb
import polars as pl
import requests
from pysolr import Solr


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

    ## Temporal alignment ##
    # Convert the column to ISO datetime format
    df = df.with_columns(
        pl.col("datePublished").str.strptime(pl.Datetime, format="%Y-%m-%d", strict=False).alias("datePublished")
    )

    df = df.with_columns(
        pl.col("dateModified").str.strptime(pl.Datetime, format="%Y-%m-%d", strict=False).alias("dateModified")
    )


    # Save to CSV
    df.write_csv(sink)

    db = lancedb.connect("./stores/lancedb")

    # Create or get LanceDB table and write data
    table = db.create_table(table, data=df, mode="overwrite")
    print(table)

# TODO:   here is there the geo and temportal processing needs to happen

def group_mode(source, sink):
    """Handle group mode operations"""
    print(f"Group mode: Processing data from {source} to {sink}")
    # Add group-specific logic here

    db = lancedb.connect("./stores/lancedb")
    table = db.open_table(source)
    arrow_table = table.to_arrow()

    # r = duckdb.query("SELECT * FROM arrow_table LIMIT 10")
    # print(r)

    conn = duckdb.connect()
    conn.register("arrow_table", arrow_table)
    explain_query = "EXPLAIN SELECT * FROM arrow_table LIMIT 10"
    result = conn.sql(explain_query)

    # Get the column names
    columns = conn.execute("PRAGMA table_info('arrow_table')").fetchall()
    column_names = [col[1] for col in columns]

    # Assuming 'ID' is the column you want to group by
    id_column = 'id'
    other_columns = [col for col in column_names if col != id_column]

    # Create list aggregation for other columns with unique values
    agg_columns = ', '.join([
        f'STRING_AGG(DISTINCT {col} ) AS list_{col}' for col in other_columns
    ])

    # Adjust the aggregation logic  NOTE:  this seems to have issues
    # agg_columns = ', '.join([
    #     # For specific columns, use FIRST_VALUE to get only the first value
    #     f'FIRST_VALUE({col}) AS first_{col}' if col in ['datePublished', 'dateModified'] else
    #     # For other columns, use STRING_AGG to return a list
    #     f'STRING_AGG(DISTINCT {col}) AS list_{col}' for col in other_columns
    # ])


    # Construct the full query
    query = f"""
        SELECT {id_column}, {agg_columns}
        FROM arrow_table
        GROUP BY {id_column}
        """

    df = conn.execute(query).fetchdf()

    # save results to a file (make an optional)
    df.to_csv(sink)

    # Create or get LanceDB table and write data
    table = db.create_table(f"{source}_grouped", data=df, mode="overwrite")
    print(table)

def jsonl_mode(source):
    """Handle JSONL mode operations"""
    print(f"JSONL mode: Processing data from lancedb table {source} to a file")
    # Add JSONL-specific logic here

    dblocation = "./stores/lancedb"
    table_name = source

    # def lance_to_jsonl(table_name, uri, output_jsonl):
    """
    Convert a LanceDB table to a JSONL file
    Args:
    table_name (str): Name of the LanceDB table
    uri (str): URI of the LanceDB database
    output_jsonl (str): Path to the output JSONL file
    """
    # Connect to LanceDB
    db = lancedb.connect(dblocation)
    table = db[table_name]
    output_jsonl = f"./stores/solrInputFiles/{table_name}.jsonl"

    # Open JSONL file for writing
    with open(output_jsonl, 'w') as jsonlfile:
        # Convert each row to JSON
        for row in table.to_pandas().to_dict('records'):
            jsonlfile.write(json.dumps(row) + '\n')

    print(f"Converted table {table_name} to {output_jsonl}")

def table_mode(source, sink):
    """Handle table mode operations"""
    print(f"Table mode: Processing data from {source} to {sink}")
    # Add table-specific logic here


    if not Path(source).is_file():
        sys.exit(f"Error: File {source} does not exist.")

    counter = 0
    with open(source, 'r') as f:
        for line in f:
            counter += 1
            try:
                # Create Solr update document
                doc = json.loads(line)
                solr_doc = {"add": {"doc": doc}}

                # Send to Solr
                print(f"Processing line {counter}...")
                response = requests.post(
                    sink,
                    json=solr_doc,
                    headers={"Content-Type": "application/json"}
                )
                response.raise_for_status()
                print(f"Line {counter} uploaded successfully.")

            except Exception as e:
                print(f"Error uploading line {counter}: {str(e)}")

    print(f"Finished processing {counter} lines from {source}")

def batch_mode(source, sink, batch_size=1000, commit_within=1000):
    """
    Loads a JSONL file into Solr using the batch API.

    Args:
    solr_url: The URL of your Solr server (e.g., 'http://localhost:8983/solr/my_core').
    jsonl_file: The path to the JSONL file.
    batch_size: The number of documents to send in each batch.
    commit_within: The maximum time in milliseconds before a commit is performed.

    Returns:
    None
    """

    solr = Solr(sink)
    docs = []

    with open(source, 'r') as f:
        for line in f:
            doc = json.loads(line)
            docs.append(doc)

            if len(docs) >= batch_size:
                try:
                    solr.add(docs, commitWithin=commit_within)
                    docs = []
                except Exception as e:
                  print(f"Error during bulk insert: {e}")
                  raise

    if docs:  # Add any remaining documents
        try:
            solr.add(docs, commitWithin=commit_within)
        except Exception as e:
            print(f"Error during bulk insert: {e}")
            raise


def main():
    parser = argparse.ArgumentParser(description="Multi-mode data processing program")
    subparsers = parser.add_subparsers(dest="mode", help="Operation mode")

    # Query mode parser
    query_parser = subparsers.add_parser("query", help="Query mode operations")
    query_parser.add_argument("--source", required=True, help="Source file/location")
    query_parser.add_argument("--sink", required=True, help="Output destination")
    query_parser.add_argument("--query", required=True, help="SPARQL query file")
    query_parser.add_argument("--table", required=True, help="LanceDB Table name")


    # Group mode parser
    group_parser = subparsers.add_parser("group", help="Group mode operations")
    group_parser.add_argument("--source", required=True, help="Source file/location")
    group_parser.add_argument("--sink", required=True, help="Output destination")

    # JSONL mode parser
    jsonl_parser = subparsers.add_parser("jsonl", help="JSONL mode operations")
    jsonl_parser.add_argument("--source", required=True, help="Source file/location")
    # jsonl_parser.add_argument("--sink", required=True, help="Output destination")

    # Table mode parser
    table_parser = subparsers.add_parser("table", help="Table mode operations")
    table_parser.add_argument("--source", required=True, help="Source file/location")
    table_parser.add_argument("--sink", required=True, help="Output destination")

    # Batch mode parser
    batch_parser = subparsers.add_parser("batch", help="Batch mode operations")
    batch_parser.add_argument("--source", required=True, help="Source file/location")
    batch_parser.add_argument("--sink", required=True, help="Output destination")

    args = parser.parse_args()

    if args.mode is None:
        parser.print_help()
        sys.exit(1)

    # Set up connections
    # Connect to LanceDB (or do in the defs?)
    # db = lancedb.connect("./lancedb")

    # Mode selection
    mode_handlers = {
        "query": query_mode,
        "group": group_mode,
        "jsonl": jsonl_mode,
        "table": table_mode,
        "batch": batch_mode
    }

    # Execute the selected mode with appropriate parameters
    if args.mode == "query":
        mode_handlers[args.mode](args.source, args.sink, args.query, args.table)
    elif args.mode == "jsonl":
        mode_handlers[args.mode](args.source)
    else:
        mode_handlers[args.mode](args.source, args.sink)

if __name__ == "__main__":
    main()
