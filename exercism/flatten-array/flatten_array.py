def flatten(iterable):
    def flatting(lst):
        for item in lst:
            if isinstance(item, list):
                flatting(item)
            else:
                if item != None:
                    flatten_array.append(item)
    flatten_array = []
    flatting(iterable)
    return flatten_array