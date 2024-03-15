def decode(string):
    if len(string) <= 1:
        return string
    decoded_string = ""
    digits = ""

    if string[0].isdigit():
        digits += string[0]
    else:
        decoded_string += string[0]

    for i in range(1, len(string)):
        if string[i].isdigit():
            digits += string[i]
        else:
            if digits == "":
                decoded_string += string[i]
            else:
                decoded_string += f"{string[i]}" * int(digits)
            digits = ""
    return decoded_string


def encode(string: str) -> str:
    if len(string) <= 1:
        return string
    encoded_string = ""
    temp_char = string[0]
    count_char = 1
    
    for i in range(1, len(string)):
        if string[i] != temp_char:
            if count_char == 1:
                encoded_string += temp_char
            else:
                encoded_string += str(count_char) + temp_char
            temp_char = string[i]
            count_char = 1
        else:
            count_char += 1
    if count_char == 1:
        encoded_string += temp_char
    else:
        encoded_string += str(count_char) + temp_char
    return encoded_string