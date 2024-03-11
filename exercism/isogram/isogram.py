def is_isogram(string: str):
    clean_sentence = [char for char in string.lower() if char.isalpha()]
    return len(clean_sentence) == len(set(clean_sentence))