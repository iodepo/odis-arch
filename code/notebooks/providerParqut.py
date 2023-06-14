import duckdb

url = "http://ossapi.oceaninfohub.org/public/combined.parquet"
duckdb.install_extension("httpfs")

# Instantiate the DuckDB connection
con = duckdb.connect()
# con.execute("CREATE TABLE my_table AS SELECT * FROM read_parquet('{}')".format(url))  # load from url
con.execute("CREATE TABLE my_table AS SELECT * FROM read_parquet('../../secret/combined.parquet')") # load from local parquet

# Now you can execute SQL queries on the Parquet file as if it was a regular table
# r = con.execute("SELECT DISTINCT provder FROM my_table").fetchdf()
r = con.execute(" SELECT DISTINCT provder, ANY_VALUE(s),  COUNT(*) AS count FROM my_table GROUP BY provder order by count desc").fetchdf()
print(r)

r = con.execute(" SELECT keywords, COUNT(*) AS count FROM my_table WHERE keywords <> 'NaN' GROUP BY keywords order by count desc").fetchdf()
print(r)

r = con.execute(" SELECT SUM(count) AS total_count FROM ( SELECT DISTINCT keywords, COUNT(*) AS count FROM my_table WHERE keywords <> 'NaN' GROUP BY keywords order by count desc) AS counts").fetchdf()
print(r)

r = con.execute(" SELECT type, COUNT(*) AS count FROM my_table GROUP BY type order by count desc").fetchdf()
print(r)

