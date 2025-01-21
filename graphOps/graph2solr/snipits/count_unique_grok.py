import polars as pl

# Sample DataFrame
df = pl.DataFrame({
    'values': ['a,b,c', 'b,c,d,e', 'b,e']
})

# Split the string on commas to get lists of values
df = df.with_columns(pl.col('values').str.split(",").alias("split_values"))

# Flatten the list of lists into a single list, then count unique occurrences
unique_counts = df.select(
    pl.col('split_values').explode().value_counts(sort=True)
)

# Convert to a more readable dictionary form
# result = dict(zip(unique_counts['split_values'], unique_counts['counts']))

print(unique_counts)

# print(result)
