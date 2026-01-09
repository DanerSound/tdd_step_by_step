
def is_valid(list_of_numbers):
    valid_array = True
    for num in list_of_numbers:
        if type (num) not in [int, float]:
            valid_array = False

    return valid_array


def custom_sum(list_of_numbers):

    if is_valid(list_of_numbers):
        if len(list_of_numbers)!=0:
            if len(list_of_numbers) == 1:
                return list_of_numbers[0]

            total = 0
            for number in list_of_numbers:
                total = total + number

            return total
        else:
            raise TypeError (" The list can be empty")
    else:
        raise ValueError(" the array may contain not only numbers, check it")