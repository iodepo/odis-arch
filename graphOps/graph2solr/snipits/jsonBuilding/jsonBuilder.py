import json
from datetime import datetime

# Sample input data - list of dictionaries
sample_data = [
    {"id": 1, "name": "John", "age": 30, "city": "New York", "active": True},
    {"id": 2, "name": "Jane", "age": 25, "city": "Boston", "active": False},
    {"id": 3, "name": "Bob", "age": 35, "city": None, "active": True},
    {"id": 4, "name": "Alice", "age": 28, "city": "New York", "active": True}
]

def process_data(data_list):
    # Initialize our output structure
    output = {
        "metadata": {
            "processed_at": datetime.now().isoformat(),
            "total_records": len(data_list),
            "active_records": 0
        },
        "active_users": [],
        "cities": {}
    }
    
    # Process each record
    for record in data_list:
        # Count and collect active users
        if record.get("active", False):
            output["metadata"]["active_records"] += 1
            
            # Create a simplified user record
            user_info = {
                "user_id": record["id"],
                "name": record["name"]
            }
            # Only add location if city is not None
            if record["city"] is not None:
                user_info["location"] = record["city"]
            
            output["active_users"].append(user_info)
            
            # Group users by city (only if city exists)
            if record["city"] is not None:
                city = record["city"]
                if city not in output["cities"]:
                    output["cities"][city] = {
                        "count": 0,
                        "users": []
                    }
                output["cities"][city]["count"] += 1
                output["cities"][city]["users"].append(record["name"])
    
    return output

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

# Process the data and save to file
if __name__ == "__main__":
    # Process the data
    processed_result = process_data(sample_data)
    
    # Save to JSON file
    save_to_json(processed_result, "processed_data.json")
    
    # Print the result to console
    print("Processed data structure:")
    print(json.dumps(processed_result, indent=2))
