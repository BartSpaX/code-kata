def is_armstrong_number(number):
    num_to_str = str(number)
    return sum(int(digit) ** len(num_to_str) for digit in num_to_str) == number