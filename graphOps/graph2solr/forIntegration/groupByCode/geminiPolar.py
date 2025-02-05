import polars as pl

def group_and_aggregate_distinct_polars(csv_file, output_file):
    df = pl.read_csv(csv_file)

    # Group by 'ID' and aggregate other columns with distinct values
    grouped_df = df.group_by('s').agg(pl.col('*').list().unique())

    # Write the results to a CSV file
    grouped_df.write_csv(output_file)

# Example usage:
csv_file = 'results.csv'
output_file = 'output_grouped.csv'
group_and_aggregate_distinct_polars(csv_file, output_file)
