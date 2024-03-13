def find(search_list: list, value: int):

    first = 0
    last = len(search_list) - 1
    while first <= last:
        middle_index = (first+last) // 2
        if search_list[middle_index] == value:
            return middle_index
        elif search_list[middle_index] < value:
            first = middle_index + 1
        else:
            last = middle_index - 1
    raise ValueError("value not in array")
