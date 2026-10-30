from collections import Counter
import csv
from pathlib import Path

# Locate the dataset file
file_path = Path('data/tickets_data.csv')

# Read the CSV into Python
with file_path.open('r', encoding='utf-8-sig', newline='') as file:
    # Read the data from the file
    data = list(csv.DictReader(file))
    #print(list(data[0:2]))  # Print the list of dictionaries to inspect the data

# Count total number of tickets
print(f"Total number of tickets: {len(data)}")

# Count the number of tickets per category
category_counts = Counter(ticket['category'] for ticket in data)

# Display the results
for category, count in category_counts.items():
    print(f"Category: {category}, Count: {count}")

# Count the number of tickets per priority
priority_counts = Counter(ticket['priority'] for ticket in data)

# Display the results
for priority, count in priority_counts.items():
    print(f"Priority: {priority}, Count: {count}")