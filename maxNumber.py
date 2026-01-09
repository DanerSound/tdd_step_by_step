
def  max_of_two(first_number, second_number):
    if (type (first_number or second_number)) not in (int, float):
        raise TypeError (" The numbers to compare can not be letters")
    if first_number > second_number:
        return first_number
    return second_number