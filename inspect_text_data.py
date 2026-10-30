import csv
from pathlib import Path
from preprocess_text import preprocess_text

# Locate the dataset file
file_path = Path('data/sample_tickets.csv')

# Read the CSV into Python
with file_path.open('r', encoding='utf-8-sig', newline='') as file:
    # Read the data from the file
    data = list(csv.DictReader(file))
    
for ticket in data:
    processsed_text = preprocess_text(
        ticket['subject'], 
        ticket['description']
    )

    print('Processed Text:', processsed_text)
    print('Subcategory:', ticket['sub_category'])
