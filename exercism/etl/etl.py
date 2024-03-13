def transform(legacy_data):
    new_data = {}
    for key, values in legacy_data.items():
        for value in values:
            new_data[value.lower()] = key
    return dict(sorted(new_data.items()))