import csv
from pathlib import Path
from collections import Counter, defaultdict

# Step 1: Locate the dataset file
file_path = Path('data/tickets_data.csv')

# Read the CSV into Python
with file_path.open('r', encoding='utf-8-sig', newline='') as file:
    # Read the data from the file
    data = list(csv.DictReader(file))

# Group subcategories by their main categories
category_mapping = defaultdict(Counter)
print(type(category_mapping))

for ticket in data:
    category = ticket['category']
    sub_category = ticket['sub_category']
    category_mapping[category][sub_category] += 1

# Display Results
for category, subcategories in sorted(category_mapping.items()):
    print("\n", category)

    for subcategory, count in sorted(subcategories.items()):
        print(subcategory, ":", count)