def preprocess_text(subject, description):
    # Remove unnecesaary whitespace and convert to lowercase
    subject = subject.strip().lower()
    description = description.strip().lower()

    # Combine subject and description into a single string
    combined_text = f"{subject} {description}"
    return combined_text

# Execute this test only when running this file directly.
if __name__ == "__main__":
    subject = "  VPN Connection Failed  "
    description = " Unable to connect to VPN from my laptop. "

    result = preprocess_text(subject, description)
    print(result)