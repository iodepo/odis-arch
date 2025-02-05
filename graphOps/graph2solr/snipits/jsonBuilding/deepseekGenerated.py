import json

# Sample list of dictionaries (rows)
rows = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Paris'},
    {'name': 'Charlie', 'age': 45, 'city': 'London'}
]

# Initialize the JSON data structure
json_data = []

# Process each row to build the desired JSON structure
for row in rows:
    entry = {}
    
    # Extract and include name if present
    if 'name' in row:
        entry['name'] = row['name']
    
    # Conditionally include age based on value
    if 'age' in row and isinstance(row['age'], int):
        if row['age'] > 25:
            entry['age'] = row['age']
    
    # Manually add a new field based on age
    if 'age' in entry and entry['age'] > 30:
        entry['qualification'] = 'Senior'
    else:
        entry['qualification'] = 'Junior'
    
    # Add city conditionally, with additional processing
    if 'city' in row:
        entry['city'] = {'name': row['city']}
    
    # Append the constructed entry to json_data
    json_data.append(entry)

# Write the JSON data to a file with proper formatting
with open('output.json', 'w') as f:
    json.dump(json_data, f, indent=4)

print("JSON file has been created successfully.")
