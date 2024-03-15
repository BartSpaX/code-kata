def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if series == '':
        raise ValueError("series cannot be empty")
    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")
    list_of_slices = []
    for i in range(len(series)):
        if len(series[i:i+length]) == length:
            list_of_slices.append(series[i:i+length])
    return list_of_slices