
def frequency_letters (simple_string):
    if type(simple_string) is not str:
        raise TypeError('The input must be a string')

    freq_dict = {}
    if len(simple_string) == 0:
        return freq_dict
    else:
        for simple_char in simple_string:
            if freq_dict.get(simple_char)!= None:
                freq_dict[simple_char] += 1
            else:
                freq_dict[simple_char] = 1

    return freq_dict