def valid_array(list_check):
    valid = True
    for element in list_check:
        if type(element) not in [str]:
            valid = False
            return valid

    return valid

def listsLens(list_to_compare):
    lens=[]

    if len(list_to_compare)==0:
        lens.append(len(list_to_compare))
        return lens

    if valid_array(list_to_compare):
        for item in list_to_compare:
            lens.append(len(item))
    else:
        raise TypeError(" List must contain non string elements!")

    return lens