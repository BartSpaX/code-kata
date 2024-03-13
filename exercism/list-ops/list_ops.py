def append(list1: list, list2: list):
    return list1 + list2


def concat(lists: list):
    new_list = []
    for element in lists:
        new_list = append(new_list, element)
    return new_list


def filter(function, list: list):
    new_list = []
    for element in list:
        if function(element):
            new_list = append(new_list, [element])
    return new_list


def length(list: list):
    length_of_list = 0
    for _ in list:
        length_of_list += 1
    return length_of_list


def map(function, list: list):
    new_list = []
    for element in list:
        new_element = function(element)
        new_list = append(new_list, [new_element])
    return new_list


def foldl(function, list: list, initial: int):
    while list:
        initial = function(initial, list.pop(0))
    return initial


def foldr(function, list: list, initial: int):
    while list:
        initial = function(initial, list.pop())
    return initial


def reverse(list: list):
    return list[::-1]