import duckdb
import lancedb

# Review: https://duckdb.org/2021/12/03/duck-arrow.html

db = lancedb.connect("../stores/lancedb")
table = db.open_table("sparql_results")
arrow_table = table.to_arrow()

# r = duckdb.query("SELECT * FROM arrow_table LIMIT 10")
# print(r)

conn = duckdb.connect()
conn.register("arrow_table", arrow_table)
explain_query = "EXPLAIN SELECT * FROM arrow_table LIMIT 10"
result = conn.sql(explain_query)
print(result)

