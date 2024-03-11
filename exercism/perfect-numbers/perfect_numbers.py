def classify(number: int):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
        
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    
    if sum == number:
        return 'perfect'
        
    if sum < number:
        return 'deficient'
        
    return 'abundant'