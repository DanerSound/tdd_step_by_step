"""
Esercizio 008
Generatore di Istogrammi
Scrivi una semplice funzione che, data una lista di numeri, fornisca in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.

Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:

***

*******

*********

*****

"""

def valid_array(array_of_numbers):
    valid_array = True
    for number in array_of_numbers:
        if type(number) not in [int] or number < 0:
            valid_array = False

    return valid_array


def istogramGenerartor(number_list):
    if len(number_list)==0:
        raise ValueError(" The list must have at least one element")
    elif not valid_array(number_list):
        raise ValueError(" all elements must be integers")
    else:
        istogram = []
        for number in number_list:
            istogram.append("*"*number)

        return istogram
