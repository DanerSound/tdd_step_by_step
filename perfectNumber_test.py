"""
Un numero perfetto è un numero naturale uguale alla somma dei suoi divisori positivi, escluso sé stesso. Scrivi una funzione che verifichi se un numero è perfetto oppure no.

test_GIVEN_6_WHEN_checked_THEN_return_True
test_GIVEN_28_WHEN_checked_THEN_return_True

test_GIVEN_1_WHEN_checked_THEN_return_False
test_GIVEN_a_prime_number_WHEN_checked_THEN_return_False
test_GIVEN_a_non_perfect_WHEN_checked_THEN_return_False

test_GIVEN_0_WHEN_checked_THEN_raise_ValueError
test_GIVEN_negative_number_WHEN_checked_THEN_raise_ValueError
test_GIVEN_non_int_type_WHEN_checked_THEN_raise_TypeError

"""

import unittest

from perfectNumber import is_perfect

class TestPerfectNumber(unittest.TestCase):

    def test_GIVEN_6_WHEN_checked_THEN_return_True(self):
        valid_input = 6

        self.assertTrue(is_perfect(valid_input))

    def test_GIVEN_28_WHEN_checked_THEN_return_True(self):
        valid_input = 28

        self.assertTrue(is_perfect(valid_input))

    def test_GIVEN_1_WHEN_checked_THEN_return_False(self):
        valid_input = 1

        self.assertFalse(is_perfect(valid_input))

    def test_GIVEN_a_prime_number_WHEN_checked_THEN_return_False(self):
        prime_number = 5

        self.assertFalse(is_perfect(prime_number))

    def test_GIVEN_a_non_perfect_WHEN_checked_THEN_return_False(self):
        not_perfect_number = 25

        self.assertFalse(is_perfect(not_perfect_number))

    def test_GIVEN_0_WHEN_checked_THEN_raise_ValueError(self):
        invalid_input = 0

        with self.assertRaises(ValueError):
            is_perfect(invalid_input)

    def test_GIVEN_negative_number_WHEN_checked_THEN_raise_ValueError(self):
        invalid_input = -5

        with self.assertRaises(ValueError):
            is_perfect(invalid_input)

    def test_GIVEN_non_int_type_WHEN_checked_THEN_raise_TypeError(self):
        invalid_input = "A"

        with self.assertRaises(TypeError):
            is_perfect(invalid_input)
