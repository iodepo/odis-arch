import polars as pl

def count_unique_values(df: pl.DataFrame, column_name: str) -> pl.DataFrame:
    """
    Count unique values in a comma-separated string column efficiently.

    Args:
        df: Polars DataFrame
        column_name: Name of the column containing comma-separated strings

    Returns:
        Polars DataFrame with value counts
    """
    return (
        df
        .select(
            pl.col(column_name)
            .str.split(",")
            .alias("split_values")
        )
        .explode("split_values")
        .group_by("split_values")
        .count()
        .sort("count", descending=True)
    )

# Example usage:
df = pl.DataFrame({
    "tags": ["a,b,c", "b,c,d,e", "b,e"]
})

result = count_unique_values(df, "tags")
print(result)

