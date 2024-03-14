PLAIN = "abcdefghijklmnopqrstuvwxyz"
CIPHER = str.maketrans(PLAIN, PLAIN[::-1], " ,.")

def encode(plain_text: str):
    cipher_text = plain_text.lower().translate(CIPHER)
    return " ".join(cipher_text[i:i+5] for i in range(0, len(cipher_text), 5))


def decode(ciphered_text):
    return ciphered_text.translate(CIPHER)