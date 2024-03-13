def sum_of_multiples(limit, multiples):
    numbers = []
    if len(multiples) == 1 and multiples[0] == 0:
        return 0
    for multiple in multiples:
        if multiple != 0:
            for i in range(0, limit, multiple):
                numbers.append(i)
    return sum(set(numbers))