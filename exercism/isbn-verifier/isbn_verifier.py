def is_valid(isbn: str):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10:
        return False
    for char in isbn[:-1]:
        if not char.isnumeric():
            return False
    if isbn[-1].isnumeric() or isbn[-1].endswith('X'):
        multiply = 10
        result = 0
        isbn = [char.replace('X', '10') for char in isbn]
        for index in range(len(isbn)):
            result += int(isbn[index]) * multiply
            multiply -= 1
        if result % 11 != 0:
            return False
        return True
    return False