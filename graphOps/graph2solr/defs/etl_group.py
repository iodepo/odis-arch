import hashlib
from datetime import date

import duckdb
import lancedb


def compute_md5(value):
    if value is None:
        return None
    return hashlib.md5(value.encode()).hexdigest()

def group_mode(source, sink):
    print(f"Group mode: Processing data from {source} to {sink}")

    db = lancedb.connect("./stores/lancedb")
    table = db.open_table(source)
    arrow_table = table.to_arrow()

    conn = duckdb.connect()
    conn.register("arrow_table", arrow_table)

    # Get the column names
    # columns = conn.execute("PRAGMA table_info('arrow_table')").fetchall()
    # column_names = [col[1] for col in columns]

    # Read the SPARQL query from a file
    with open("./SPARQL/duckdbSQL.sql", "r") as file:
        query = file.read()

    df = conn.execute(query).fetchdf()

    # TODO  remove to augmentation
    df['index_id'] = df['id'].apply(compute_md5)
    df["indexed_ts"] = date.today().isoformat() # Add a new column with today's date in ISO format
    df["json_source"] = """{"@context": "https://schema.org/", "@type": "Person", "name": "John Doe" }"""

    # save results to a file (make an optional)
    # df.to_csv(sink)
    print("Saving Parquet")
    df.to_parquet("./stores/testgroupout.parquet")

    # Create or get LanceDB table and write data
    print("Saving Lance")
    db.create_table(f"{source}_grouped", data=df, mode="overwrite")

