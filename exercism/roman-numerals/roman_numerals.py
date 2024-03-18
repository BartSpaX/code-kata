import math

def roman(number):
    roman_dict = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M"
    }

    div = 1
    while number >= div:
        div *= 10
    div /= 10

    result = ""

    while number:
        last_number = int(number / div)
        if last_number <= 3:
            result += (roman_dict[div] * last_number)
        elif last_number == 4:
            result += (roman_dict[div] + roman_dict[div * 5])
        elif 5 <= last_number <= 8:
            result += (roman_dict[div * 5] + (roman_dict[div] * (last_number -5)))
        elif last_number == 9:
            result += (roman_dict[div] + roman_dict[div * 10])
        number = math.floor(number % div)
        div /= 10
    return result