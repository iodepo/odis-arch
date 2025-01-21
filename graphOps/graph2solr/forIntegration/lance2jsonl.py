import lancedb
import json

# Connect to LanceDB
db = lancedb.connect("./lancedb")
table = db.open_table("sparql_results")

# Convert to DataFrame and then to JSONL
df = table.to_pandas()
df.to_json("output.jsonl", orient="records", lines=True)

print(f"Converted {len(df)} records to JSONL format")

