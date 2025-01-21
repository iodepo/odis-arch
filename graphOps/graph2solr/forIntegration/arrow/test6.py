import pyarrow as pa
import pyarrow.compute as pc

# Define the input table
table = pa.table([
    pa.array(["a", "a", "b", "b", "b", "c", "d", "d", "e", "c"]),
    pa.array(["a1", "a2", "b1", "b2", "b3", "c1", "d1", "d2", "e1", "c2"]),
], names=["keys", "values"])

# Disable multithreading since I guess first doesn't like it
pa.set_cpu_count(1)

# Filter for key 'b' and get the first value as a test of that
b_mask = pc.equal(table["keys"], "b")
b_table = table.filter(b_mask).group_by("keys").aggregate([
    ("keys", "first", "values")  # Specify output column name 'values'
])

# Re-enable multithreading
pa.set_cpu_count(6)  # tried () to reset..  didn't seem to work, try 0

# Filter for other keys and get lists
not_b_mask = pc.invert(b_mask)
other_table = table.filter(not_b_mask).group_by("keys").aggregate([
    ("keys", "list", "values")  # Specify output column name 'values'
])

# Convert 'values' in b_table to lists to match the data type in other_table
from pyarrow import list_

# Wrap the 'values' column in b_table into a list
b_values_as_list = pa.array([[value] for value in b_table.column('values')], type=pa.list_(pa.string()))

# Replace the 'values' column in b_table with the list-wrapped version
b_table = b_table.set_column(
    b_table.schema.get_field_index('values'),
    'values',
    b_values_as_list
)

# Now the schemas match, and you can concatenate the tables
result = pa.concat_tables([b_table, other_table])

print(result)
