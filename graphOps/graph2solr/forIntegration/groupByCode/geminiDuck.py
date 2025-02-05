import pandas as pd
import duckdb

def group_and_aggregate(csv_file):
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Identify the index of the 'ID' column
    id_index = df.columns.get_loc('ID')

    # Get the names of other columns
    other_columns = df.columns[df.columns != 'ID']

    # Construct the SQL query dynamically
    query = f"""
    SELECT
        ID,
        {', '.join(f'LIST_AGG({col}) AS {col}' for col in other_columns)}
    FROM
        df
    GROUP BY
        ID;
    """

    # Create a DuckDB connection
    conn = duckdb.connect()

    # Register the DataFrame as a table
    conn.register('df', df)

    # Execute the query
    result = conn.execute(query).fetchdf()

    return result

# Example usage:
csv_file = 'your_csv_file.csv'
grouped_df = group_and_aggregate(csv_file)
print(grouped_df)

