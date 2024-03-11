def is_pangram(sentence: str):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p','q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for char in alphabet:
        if char not in sentence.lower():
            return False
    return True