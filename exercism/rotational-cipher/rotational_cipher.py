def rotate(text: str, key: int):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_alphabet = alphabet[key:] + alphabet[:key]
    transform = str.maketrans(alphabet + alphabet.upper(), new_alphabet + new_alphabet.upper())
    return text.translate(transform)