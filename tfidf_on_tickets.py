import csv
from pathlib import Path
from preprocess_text import preprocess_text
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Locate the dataset file
file_path = Path('data/sample_tickets.csv')

# Read the CSV into Python
with file_path.open('r', encoding='utf-8-sig', newline='') as file:
    # Read the data from the file
    data = list(csv.DictReader(file))

# Step 1: Extract the text data from the tickets
processed_texts = [preprocess_text(ticket['subject'], ticket['description']) for ticket in data]

# Step 2: Target labels (categories) for each ticket
labels = [ticket['category'] for ticket in data]

# Step 3: Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(processed_texts)

# Step 4: Define the target variable (y) based on the category of each ticket
y = labels

# # View the results into a DataFrame for better visualization
# df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
# df['category'] = [ticket['category'] for ticket in data]
# print(df.head(7))

# Step 5: Display the results

print(len(vectorizer.get_feature_names_out()))

print("\nTF-IDF scores for the first ticket:")
print(X[0].toarray().round(3))

print("Total documents:", len(processed_texts))
print("Vocabulary size:", len(vectorizer.get_feature_names_out()))
print("Feature matrix shape:", X.shape)
print("Total target labels:", len(y))

# print('\nidf values:')
# for ele1, ele2 in zip(vectorizer.get_feature_names_out(), vectorizer.idf_):
#     print(ele1, ':', ele2.round(3))
