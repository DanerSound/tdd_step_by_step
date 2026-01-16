"""
Esercizio 006
Moltiplicatore Inarrestabile
Scrivi un programma "moltiplicatore" che, data una lista di numeri, moltiplichi tra loro tutti gli elementi.
"""

def valid_array(array_of_numbers):
    valid_array = True
    for number in array_of_numbers:
        if type(number) not in [int, float]:
            valid_array = False

    return valid_array


def custom_mul(list_of_numbers):
    if valid_array(list_of_numbers):
        if 0 in list_of_numbers:
            return 0
        else:
            if len(list_of_numbers) == 0:
                raise ValueError("The list can be empty")
            elif len(list_of_numbers) == 1:
                return list_of_numbers[0]
            else:
                result = 1
                for number in list_of_numbers:
                    result *= number

                return result
    else:
        raise ValueError("The list must have only numeric elements")