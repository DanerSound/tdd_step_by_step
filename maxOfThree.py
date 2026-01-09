
first_number = int(input("Insert the first number: "))
second_number = int(input("Insert the second number: "))
third_number = int(input("Insert the third number: "))


def max_of_three(first, second, third):
    if (type (first or second or third))not in [int, float]:
        raise TypeError (" all the inserted numbers must be integers ")

    if first >= second and first >= third:
        return first
    elif second >= first and second >= third:
        return second
    elif third >= first and third >= first:
        return third
    return None
