def rows(letter: str):
    letters = [chr(x) for x in range(ord('A'), ord(letter) + 1)]
    alphabet = letters[:-1] + letters[::-1]
    diamond = letters[::-1] + letters[1:]
    return [''.join(x if x == y else ' ' for y in diamond) for x in alphabet]