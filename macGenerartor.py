
import random
from unittest.util import unorderable_list_difference


def mac_generator():
    numbers = [0,1,2,3,4,5,6,7,8,9]
    hexa = ['A', 'B', 'C', 'D', 'E', 'F']
    uno = f"{random.choice(numbers)}{random.choice(numbers)}"
    due = f"{random.choice(hexa)}{random.choice(hexa)}"
    tre = f"{random.choice(hexa)}{random.choice(numbers)}"
    quattro = f"{random.choice(hexa)}{random.choice(numbers)}"
    cinque = f"{random.choice(numbers)}{random.choice(numbers)}"
    sei = f"{random.choice(numbers)}{random.choice(numbers)}"
    mac = f"{uno}:{due}:{tre}:{quattro}:{cinque}:{sei}"
    return mac