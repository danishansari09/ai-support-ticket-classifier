from sklearn.feature_extraction.text import TfidfVectorizer

# Step 1: Sample ticket descriptions
texts = [
    "vpn connection failed",
    "vpn access failed",
    "wifi connection failed",
    "vpn vpn connection failed"
]

# Step 2: Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Step 3: Fit the vectorizer to the texts and transform them into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(texts)
# Step 4: Display the vocabulary
print("Vocabulary:")
print(vectorizer.get_feature_names_out())

# Step 5: Display the TF-IDF matrix
print("\nTF-IDF Matrix:")
print(tfidf_matrix.toarray().round(3))

# Step 6: Display the IDF score for each word
print("\nIDF Scores:")

for word, score in zip(
    vectorizer.get_feature_names_out(),
    vectorizer.idf_
):
    print(word, ":", round(score, 3))
