import pyarrow as pa
import pyarrow.compute as pc

def aggregate_string_columns(table):
    """
    Aggregates string columns in an Arrow table by ID, concatenating name and keyword
    while keeping first instance of usage.
    
    Args:
        table: PyArrow Table with columns 'id', 'name', 'keyword', 'usage'
        
    Returns:
        PyArrow Table with aggregated results
    """
    # First, let's make a dictionary to store our first usage values
    # We'll get this before grouping to ensure we get the first occurrence
    id_to_first_usage = {}
    ids = table.column('id').to_pylist()
    usages = table.column('usage').to_pylist()
    for id_val, usage in zip(ids, usages):
        if id_val not in id_to_first_usage:
            id_to_first_usage[id_val] = usage

    # Group by ID
    keys = ['id']
    
    # Define aggregations for the string columns
    aggregations = [
        ('name', 'list'),
        ('keyword', 'list')
    ]
    
    # Perform the grouping
    grouped = table.group_by(keys).aggregate(aggregations)
    
    # Convert the list columns back to concatenated strings
    result = grouped
    
    # Join the string lists with commas
    result = result.set_column(
        1,  # index of 'name' column
        'name',
        pc.list_join(result.column('name'), ', ')
    )
    
    result = result.set_column(
        2,  # index of 'keyword' column
        'keyword',
        pc.list_join(result.column('keyword'), ', ')
    )
    
    # Add back the first usage values
    first_usages = [id_to_first_usage[id_val] for id_val in result.column('id').to_pylist()]
    result = result.append_column('usage', pa.array(first_usages))
    
    return result

# Example usage
data = {
    'id': ['1', '1', '2', '2', '2'],
    'name': ['John', 'Johnny', 'Alice', 'Al', 'A'],
    'keyword': ['tech', 'programming', 'art', 'design', 'creative'],
    'usage': ['high', 'medium', 'low', 'medium', 'high']
}

# Create Arrow table
table = pa.Table.from_pydict(data)

# Perform aggregation
result = aggregate_string_columns(table)

# Print results
print(result.to_pandas())

