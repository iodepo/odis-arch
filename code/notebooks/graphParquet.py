import duckdb

url = "http://ossapi.oceaninfohub.org/public/oihgraph_rdf.parquet"
duckdb.install_extension("httpfs")

# Instantiate the DuckDB connection
con = duckdb.connect()
# con.execute("CREATE TABLE my_table AS SELECT * FROM read_parquet('{}')".format(url))  # load from url
con.execute("CREATE TABLE my_table AS SELECT * FROM read_parquet('../../secret/oihgraph_rdf.parquet')") # load from local parquet


r = con.execute(" SELECT DISTINCT predicate,  COUNT(*) AS count FROM my_table GROUP BY predicate order by count desc").fetchdf()
print(r)