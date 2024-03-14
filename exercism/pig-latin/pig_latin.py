VOWELS = ["a", "e", "i", "o", "u"]
VOWELS_Y = ["a", "e", "i", "o", "u", 'y']
SPECIAL = ["xr", "yt"]

def translate(text: str):
    pig_latin = []

    for word in text.split():
        if word[0] in VOWELS or word[0:2] in SPECIAL:
            pig_latin.append(word + "ay")
            continue
            
        for i in range(1, len(word)):
            if word[i] in VOWELS_Y:
                i += 1 if word[i] == 'u' and word[i - 1] == 'q' else 0
                pig_latin.append(word[i:] + word[:i] + "ay")
                break
    return " ".join(pig_latin)