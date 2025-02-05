import polars as pl

# Sample DataFrame
df = pl.DataFrame({
        'source': [1, 2, 6],
        'contype': ['edge type A', 'edge type B', 'edge type C'],
        'target': [[1, 2], [2, 3 ], [1, 4]]
    })

# Explode the DataFrame to get individual source-target pairs
# exploded_df = df.explode(["target"])
df_combined = df.with_columns(
            pl.concat_list(["source", "target"]).alias("all_nodes"))

# Get unique nodes from the combined list
unique_nodes = df_combined["all_nodes"].explode().unique()


# Create a new DataFrame with unique nodes and associated contype
unique_nodes_df = unique_nodes.group_by("source") \
            .agg(pl.first("contype").alias("contype")) \
            .with_columns(pl.col("source").alias("node"))

print(unique_nodes_df)
