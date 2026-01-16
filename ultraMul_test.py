import unittest

from ultraMul import custom_mul

"""
1. GIVEN_list_of_valid_numbers_WHEN_multiplied_THEN_return_product
2. GIVEN_list_with_one_element_WHEN_multiplied_THEN_return_that_element
3. GIVEN_empty_list_WHEN_multiplied_THEN_raise_error
4. GIVEN_list_with_non_numeric_elements_WHEN_multiplied_THEN_raise_error
5. GIVEN_list_containing_zero_WHEN_multiplied_THEN_return_zero
6. GIVEN_list_with_even_number_of_negative_numbers_WHEN_multiplied_THEN_return_positive
7. GIVEN_list_with_odd_number_of_negative_numbers_WHEN_multiplied_THEN_return_negative
8. GIVEN_list_of_floats_WHEN_multiplied_THEN_return_correct_product
"""

class Test(unittest.TestCase):

    def test_GIVEN_list_of_valid_numbers_WHEN_multiplied_THEN_return_product (self):
        #arrage
        valid_list = [1, 2, 3, 4, 5, 6]

        #act
        valid_mult = custom_mul(valid_list)

        #assert
        self.assertEqual(valid_mult, 720)

    def test_GIVEN_list_with_one_element_WHEN_multiplied_THEN_return_that_element(self):
        single_element_list = [6]

        valid_mult = custom_mul(single_element_list)

        self.assertEqual(valid_mult, 6)

    def test_GIVEN_empty_list_WHEN_multiplied_THEN_raise_error(self):
        empty_list = []

        with self.assertRaises(ValueError):
            custom_mul(empty_list)

    def test_GIVEN_list_with_non_numeric_elements_WHEN_multiplied_THEN_raise_error(self):

        generic_array = [1, 0, -3, 2 + 5j, True, "letter", 7.3, 8]

        with self.assertRaises(ValueError):
            custom_mul(generic_array)

    def test_GIVEN_list_containing_zero_WHEN_multiplied_THEN_return_zero(self):

        valid_list = [1, 2, 3, 0, 5, 6]

        result = custom_mul(valid_list)

        self.assertEqual(result, 0)

    def test_GIVEN_list_with_even_number_of_negative_numbers_WHEN_multiplied_THEN_return_positive(self):

        even_negative_numbers = [-1, -2, -3, - 4]

        result = custom_mul(even_negative_numbers)

        self.assertEqual(result, 24)

    def test_GIVEN_list_with_odd_number_of_negative_numbers_WHEN_multiplied_THEN_return_negative(self):

        odd_negative_numbers = [-1, -2, -3]

        result = custom_mul(odd_negative_numbers)

        self.assertEqual(result, -6)

    def test_GIVEN_list_of_floats_WHEN_multiplied_THEN_return_correct_product(self):

        float_list = [3.2, 5.4, 6.2]

        result = custom_mul(float_list)

        self.assertEqual(round(result,2), 107.14)