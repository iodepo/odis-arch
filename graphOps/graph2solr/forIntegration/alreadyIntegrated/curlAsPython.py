import requests
import polars as pl
import lancedb
from io import StringIO

# Connect to LanceDB
db = lancedb.connect("./lancedb")

url = "http://0.0.0.0:7019"
params = {
            "timeout": "600s",
                "access-token": "odis_7643543846_6dMISzlPrD7i"
        }
headers = {
            "Accept": "text/csv",
            "Content-type": "application/sparql-query"
        }

# Read the SPARQL query from file
with open("../SPARQL/baseQuery.rq", "r") as file:
        query = file.read()

# Send the request
response = requests.post(url, params=params, headers=headers, data=query)

# Load response into Polars DataFrame
df = pl.read_csv(StringIO(response.text))

# Save to CSV
df.write_csv("results_sparql.csv")

# Create or get LanceDB table and write data
table = db.create_table("sparql_results", data=df, mode="overwrite")
print(df.head(10))
