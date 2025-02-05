import pyarrow as pa
import pyarrow.compute as pc

# Define the input table
table = pa.table([
    pa.array(["a", "a", "b", "b", "b", "c", "d", "d", "e", "c"]),
    pa.array(["a1", "a2", "b1", "b2", None, "c1", "d1", "", "e1", "c2"]),
], names=["keys", "values"])


# Create a mask to filter out None and empty string values
mask = pc.and_(
    pc.is_valid(table['values']),  # Exclude None values
    pc.not_equal(table['values'], "")  # Exclude empty strings
)

# Filter the table using the mask
filtered_table = table.filter(mask)

# Group by keys and aggregate values into lists
other_table = filtered_table.group_by("keys").aggregate([
    ("values", "list")
])

print(other_table)