def find_anagrams(word: str, candidates: list[str]):
    return [i for i in candidates if sorted(i.lower()) == sorted(word.lower()) and i.lower() != word.lower()]