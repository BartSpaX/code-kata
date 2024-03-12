def label(colors: list[str]) -> str:
    bands = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }
    value = ""
    if len(colors) > 3:
        colors = colors[:-1]
    for color in colors[:-1]:
        value += str(bands[color])
    multiply = int("1"+"0"*bands[colors[-1]])
    resistance = int(value) * multiply
    if resistance >= 1000000000:
        resistance //= 1000000000
        return f'{resistance} gigaohms'
    elif resistance >= 1000000:
        resistance //= 1000000
        return f'{resistance} megaohms'
    elif resistance >= 1000:
        resistance //= 1000
        return f'{resistance} kiloohms'
    return f'{resistance} ohms'

