import duckdb

# Establish a connection to DuckDB
con = duckdb.connect(':memory:')

# Path to the CSV file
csv_file_path = 'people_data.csv'

# Read the CSV file into a DuckDB table
con.execute(f"CREATE TABLE people AS SELECT * FROM read_csv_auto('{csv_file_path}')")

# Assuming 'ID' is the column you want to group by
id_column = 'ID'
other_columns = ['Name', 'City', 'Hobby']

# Create list aggregation for other columns using DISTINCT
agg_columns = ', '.join([f'LIST_AGGR(DISTINCT {col}) AS list_{col}' for col in other_columns])

# Construct the full query
query = f"""
SELECT {id_column}, {agg_columns}
FROM people
GROUP BY {id_column}
"""

# Execute the query and fetch results
results = con.execute(query).fetchall()

# Print results
print("\nGrouped Results:")
for row in results:
        print(row)

        # Close the connection
        con.close()
