import csv

# Sample data with duplicates to demonstrate list aggregation
data = [
    ['ID', 'Name', 'City', 'Hobby'],
    [1, 'Alice', 'New York', 'Reading'],
    [1, 'Bob', 'Chicago', 'Swimming'],
    [1, 'Alice', 'New York', 'Painting'],
    [2, 'Charlie', 'Los Angeles', 'Hiking'],
    [2, 'Charlie', 'Los Angeles', 'Hiking'],
    [2, 'David', 'San Francisco', 'Cooking']
       ]

# Write to CSV
with open('people_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

        print("CSV file 'people_data.csv' has been created.")
