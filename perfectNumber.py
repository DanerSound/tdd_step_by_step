def is_perfect(number):
    if not isinstance(number, int):
        raise TypeError('The input is not an integer.')
    if number == 0:
        raise ValueError('number is 0')
    elif number < 0:
        raise ValueError('number cant be negative')

    summ = 0
    for i in range(1,number):
        if number % i  == 0:
            summ += i
    if summ == number:
        return True
    else:
        return False