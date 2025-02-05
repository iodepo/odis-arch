import duckdb

# Establish a connection to DuckDB
con = duckdb.connect(':memory:')

# Path to your CSV file
csv_file_path = 'results_long.csv'

# Read the CSV file into a DuckDB table
con.execute(f"CREATE TABLE data AS SELECT * FROM read_csv_auto('{csv_file_path}', all_varchar=true,ignore_errors=true)")

# Get the column names
columns = con.execute("PRAGMA table_info('data')").fetchall()
column_names = [col[1] for col in columns]

# Assuming 'ID' is the column you want to group by
id_column = 's'
other_columns = [col for col in column_names if col != id_column]

# Create list aggregation for other columns with unique values
agg_columns = ', '.join([
        f'STRING_AGG(DISTINCT {col} ) AS list_{col}' for col in other_columns
])

# Construct the full query
query = f"""
SELECT {id_column}, {agg_columns}
FROM data
GROUP BY {id_column}
"""

df = con.execute(query).fetchdf()

df.to_csv('results_long_grouped.csv')
