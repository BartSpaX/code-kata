def resistor_label(colors: list[str]) -> str:
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

    tolerance = {
        "grey": "0.05%",
        "violet": "0.1%",
        "blue": "0.25%",
        "green": "0.5%",
        "brown": "1%",
        "red": "2%",
        "gold": "5%",
        "silver": "10%"
    }

    value = ""

    if len(colors) == 1:
        return f'{bands[colors[0]]} ohms'
    
    for color in colors[:-2]:
        value += str(bands[color])
    multiplier = int("1"+"0"*bands[colors[-2]])
    tol_value = tolerance[colors[-1]]
    resistance = int(value) * multiplier

    if resistance >= 1000000000:
        resistance /= 1000000000
        return f"{int(resistance) if resistance.is_integer() else resistance} gigaohms ±{tol_value}"
    elif resistance >= 1000000:
        resistance /= 1000000
        return f"{int(resistance) if resistance.is_integer() else resistance} megaohms ±{tol_value}"
    elif resistance >= 1000:
        resistance /= 1000
        return f"{int(resistance) if resistance.is_integer() else resistance} kiloohms ±{tol_value}"
    return f'{resistance} ohms ±{tol_value}'
