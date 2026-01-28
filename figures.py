from math import pi

def circle_area(radius):
    if type(radius) not in [int, float]:
        raise TypeError("radius must be a number")
    elif radius < 0:
        raise ValueError('radius cannot be negative')
    else:
        return pi * (radius ** 2)

def square_area(side):
    if type(side) not in [int, float]:
        raise TypeError("side must be a number")
    if side < 0:
        raise ValueError('side cannot be negative')
    return side ** 2

def rectangle_area(width, height):
    if (type(width or height)) not in [int, float]:
        raise TypeError("width must be a number")
    elif width < 0 or height < 0:
        raise ValueError('width or height cannot be negative')
    else:
        return width * height

def triangle_area(width, height):
    if (type(width or height)) not in [int, float]:
        raise TypeError("width must be a number")
    elif width < 0 or height < 0:
        raise ValueError('width or height cannot be negative')
    else:
        return (width * height)/2
