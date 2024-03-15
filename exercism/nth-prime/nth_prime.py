def isPrime(number):
    if number <= 1:
        return False
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    for i in range(5, 1 + int(number ** 0.5), 6):
        if number % i == 0 or number % (i + 2) == 0:
            return False
    return True

def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    i = 2
    while number > 0:
        if isPrime(i):
            number -= 1
        i += 1
    i -= 1
    return i