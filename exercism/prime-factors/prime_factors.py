import math

def factors(value):
    prime_factors = []
    
    while value % 2 == 0:
        prime_factors.append(2)
        value //= 2
    for i in range(3, int(math.sqrt(value)) + 1, 2):
        while value % i == 0:
            prime_factors.append(i)
            value //= i

    if value > 2:
        prime_factors.append(value)
    return prime_factors
