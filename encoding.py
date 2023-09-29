# Text to encode
original_text = "Hello, World! 🌍"

# Encode the text to UTF-8
encoded_text = original_text.encode('utf-8')

# Print the encoded bytes
print("Encoded Text (UTF-8):")
print(encoded_text)

# Decode the UTF-8 bytes back to text
decoded_text = encoded_text.decode('utf-8')

# Print the decoded text
print("\nDecoded Text:")
print(decoded_text)
