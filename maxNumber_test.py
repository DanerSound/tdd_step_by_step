import unittest

from maxNumber import max_of_two

class TestMaxNumber(unittest.TestCase):

    def test_GIVEN_two_valid_numbers_WHEN_first_is_greater_THEM_return_first(self):
        # Arrange
        first_number = 10
        second_number = 5

        # Act
        result = max_of_two(first_number,second_number)

        # assert
        self.assertEqual(result, 10)

    def test_GIVEN_two_valid_numbers_WHEN_second_is_greater_THEM_return_second(self):
        # Arrange
        first_number = 2
        second_number = 8

        # Act
        result = max_of_two(first_number,second_number)

        # assert
        self.assertEqual(result, 8)

    def test_GIVEN_two_equal_numbers_WHEN_compared_THEM_return_that_number(self):
        # Arrange
        first_number = 5
        second_number = 5

        # Act
        result = max_of_two(first_number,second_number)

        # Assert
        self.assertEqual(result, 5)

    def test_GIVEN_first_value_is_not_a_number_WHEN_compared_THEM_raise_error(self):
        # Arrage
        first_number = "a"
        second_number = 10

        # Act & Assert
        with self.assertRaises(TypeError):
            max_of_two(first_number, second_number)

    def test_GIVEN_second_value_is_not_a_number_WHEN_compared_THEM_raise_error(self):
        # Arrange
        first_number = 10
        second_number = "a"

        # Act & Assert
        with self.assertRaises(TypeError):
            max_of_two(first_number, second_number)