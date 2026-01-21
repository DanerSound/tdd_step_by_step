def customLen(iterable_obj):
    if type(iterable_obj) in [int, float, None]:
        raise TypeError(" the input must be iterable")

    count = 0
    for item in iterable_obj:
        count += 1

    return count