import duckdb

# Establish a connection to DuckDB
con = duckdb.connect(':memory:')

# Path to your CSV file (replace with your actual file path)
csv_file_path = 'people_data.csv'

# Read the CSV file into a DuckDB table
con.execute(f"CREATE TABLE data AS SELECT * FROM read_csv_auto('{csv_file_path}')")

# Get the column names
columns = con.execute("PRAGMA table_info('data')").fetchall()
column_names = [col[1] for col in columns]

# Assuming 'ID' is the column you want to group by
id_column = 'ID'
other_columns = [col for col in column_names if col != id_column]

# Create list aggregation for other columns using DISTINCT
agg_columns = ', '.join([f'LIST_AGG(DISTINCT {col}) AS list_{col}' for col in other_columns])

# Construct the full query
query = f"""
SELECT {id_column}, {agg_columns}
FROM data
GROUP BY {id_column}
"""

# Execute the query and fetch results
results = con.execute(query).fetchall()

# Print column names
print("Column names:", column_names)

# Print results
print("\nGrouped Results:")
for row in results:
        print(row)

        # Close the connection
        con.close()
