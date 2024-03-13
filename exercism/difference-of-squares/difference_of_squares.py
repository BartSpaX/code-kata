def square_of_sum(number):
    array = [i for i in range(1, number+1)]
    return pow(sum(array), 2)


def sum_of_squares(number):
    array = [pow(i, 2) for i in range(1, number+1)]
    return sum(array)


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)