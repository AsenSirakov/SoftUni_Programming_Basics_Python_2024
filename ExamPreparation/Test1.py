import base64

def encode_text(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')
    return encoded_text

def decode_text(encoded_text):
    decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text

if __name__ == "__main__":
    text = input("Enter text to encode: ")
    encoded_text = encode_text(text)
    print("Encoded text:", encoded_text)

    decoded_text = decode_text(encoded_text)
    print("Decoded text:", decoded_text)
