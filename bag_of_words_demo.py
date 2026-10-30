from collections import Counter

# Step 1: Our sample ticket descriptions
texts = [
    "vpn connection failed",
    "vpn access failed",
    "wifi connection failed",
    "vpn vpn connection failed"
]

# Step 2: Create a vocabulary of unique words
vocabulary = sorted(set(" ".join(texts).split()))

# Step 3: Convert every ticket into a numerical vector
for text in texts:

    word_counts = Counter(text.split())
    # print("Word Counts:", word_counts)
    vector = [word_counts[word] for word in vocabulary]
    print(text, "->", vector)
 