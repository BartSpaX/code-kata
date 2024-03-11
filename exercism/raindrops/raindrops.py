def convert(number: int):
    response = ""
    if number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
        if number % 3 == 0:
            response += "Pling"
        if number % 5 == 0:
            response += "Plang"
        if number % 7 == 0:
            response += "Plong"
    else:
        response = str(number)
    return response