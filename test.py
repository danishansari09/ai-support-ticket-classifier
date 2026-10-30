from sklearn.feature_extraction.text import TfidfVectorizer
text = ["vpn vpn vpn access failed"]

# Step 2: Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Step 3: Fit the vectorizer to the texts and transform them into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(text)
# Step 4: Display the vocabulary
print("Vocabulary:")
print(vectorizer.get_feature_names_out())
print(vectorizer.idf_)