def score(word: str):
    score_table = {
        1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }
    scores = []
    for letter in word.upper():
        for key, value in score_table.items():
            if letter in value:
                scores.append(key)
    return sum(scores)