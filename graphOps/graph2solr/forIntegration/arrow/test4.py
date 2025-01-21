import pyarrow as pa
import pyarrow.compute as pc

table = pa.table([
      pa.array(["a", "a", "b", "b", "b", "c", "d", "d", "e", "c"]),
      pa.array(["a1", "a2", "b1", "b2", "b3", "c1", "d1", "d2", "e1", "c2"]),
      ], names=["keys", "values"])

print(table)

grouped_table = table.group_by("keys").aggregate([
        ("values", "list")
    ])

print(grouped_table)

