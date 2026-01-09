def is_valid_array(input_array):
    valid_array = True
    for element in input_array:
        if not isinstance(element, int):
            valid_array = False

    return valid_array


def maxOverAll(valid_list):

    if is_valid_array(valid_list):

        if len(valid_list)==0:
            raise ValueError("list cant be Empty")
        maximus = valid_list[0]
        for num in valid_list:
            if num >= maximus:
                maximus = num

        return maximus
    else:
        raise ValueError("The array contains invalid elements")