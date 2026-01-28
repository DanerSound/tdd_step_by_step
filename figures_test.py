"""
Esercizio 014
Il Geometra
Scrivi una funzione che, a scelta dell'utente, calcoli l'area di:
un cerchio
un quadrato
un rettangolo
un triangolo
"""

import unittest

from figures import circle_area, square_area, rectangle_area, triangle_area
from math import pi


class figures_test(unittest.TestCase):

    def test_circle_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertEqual(circle_area(2.1), pi * 2.1 ** 2)

    def test_values_circle_area(self):
        # raise error when imput is invalid
        self.assertRaises(ValueError, circle_area, -2)

    def test_types_circle_area(self):
        self.assertRaises(TypeError, circle_area, 3 + 5j)
        self.assertRaises(TypeError, circle_area, True)
        self.assertRaises(TypeError, circle_area, "radius")

    def test_square_area(self):
        # Testing areas with side >=0
        self.assertEqual(square_area(0), 0)
        self.assertEqual(square_area(1), 1)
        self.assertAlmostEqual(square_area(2.1), 2.1 ** 2)

    def test_values_square_area(self):
        # raise error when input is invalid
        self.assertRaises(ValueError, square_area, -2)

    def test_types_square_area(self):
        # raise error when input is too generic
        self.assertRaises(TypeError, square_area, 3 + 5j)
        self.assertRaises(TypeError, square_area, True)
        self.assertRaises(TypeError, square_area, "side")

    def test_retangle_area(self):
        # Area when given positive height and with
        self.assertEqual(rectangle_area(2, 2), 2 * 2)
        self.assertEqual(rectangle_area(1, 1), 1)
        self.assertEqual(rectangle_area(2, 0), 0)

    def test_values_rectangle_area(self):
        self.assertRaises(ValueError, rectangle_area, -1, 1)

    def test_types_rectangle_area(self):
        # raise error when input is too generic
        self.assertRaises(TypeError, rectangle_area, 3 + 5j, 4)
        self.assertRaises(TypeError, rectangle_area, True, 2)
        self.assertRaises(TypeError, rectangle_area, "width", "height")

    def test_triangle_area(self):
        # Area when given positive height and with
        self.assertEqual(triangle_area(2, 2), (2 * 2) / 2)
        self.assertEqual(triangle_area(1, 1), 1 / 2)
        self.assertEqual(triangle_area(2, 0), 0)


    def test_values_triangle_area(self):
        self.assertRaises(ValueError, triangle_area, -1, 1)

    def test_types_triangle_area(self):
       # raise error when input is too generic
       self.assertRaises(TypeError, triangle_area, 3 + 5j, 4)
       self.assertRaises(TypeError, triangle_area, True, 2)
       self.assertRaises(TypeError, triangle_area, "width", "height")

