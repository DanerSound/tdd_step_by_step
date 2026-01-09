import unittest

from maxOfThree import max_of_three

"""
1. test_GIVEN_three_valid_numbers_WHEN_given_to_func_THEN_return_greatest
2. test_GIVEN_two_equal_numbers_WHEN_compared_THEN_return_greatest
3. test_GIVEN_any_input_not_valid_WHEN_compared_THEN_raise_error


"""

class TestMaxOfThree(unittest.TestCase):


    def test_GIVEN_three_valid_numbers_WHEN_given_to_func_THEN_return_greatest(self):
        #Arrange
        first = 1
        second = 3
        third = 3

        #Act
        result = max_of_three(first, second, third)

        #Assert
        self.assertEqual(result, 3)

    def test_GIVEN_any_input_not_valid_WHEN_compared_THEN_raise_error(self):
        #Arrange
        first = 1
        second = "a"
        third = 3

        # Act & Assert
        with self.assertRaises(TypeError) :
            max_of_three(first, second, third)

