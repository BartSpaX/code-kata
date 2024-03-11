def response(hey_bob: str):
    if hey_bob.strip().endswith('?'):
        if hey_bob.isupper():
            return str("Calm down, I know what I'm doing!")
        return str("Sure.")
    if hey_bob.isupper():
        return str("Whoa, chill out!")
    if hey_bob.strip() == "":
        return str("Fine. Be that way!")
    return str("Whatever.")