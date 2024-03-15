special_characters = ['-', ',', '.', '_']

def abbreviate(words: str) -> str:
    shortcut = ""
    for i in special_characters:
        words = words.replace(i, ' ')
    for word in words.split():
        shortcut += word[0].upper()
    return shortcut