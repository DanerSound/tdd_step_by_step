import unittest

from maxOverAll import maxOverAll
"""
1. GIVEN_list_of_valid_numbers_WHEN_compared_THEN_return_greatest
2. GIVEN_list_with_one_element_WHEN_compared_THEN_return_that_element
3. GIVEN_empty_list_WHEN_compared_THEN_raise_error
4. GIVEN_list_with_non_numeric_elements_WHEN_compared_THEN_raise_error
5. GIVEN_list_with_all_negative_elements_WHEN_compared_THEN_return_max
"""


class TestMaxOverAll(unittest.TestCase):

    def test_GIVEN_list_of_valid_numbers_WHEN_compared_THEN_return_greatest(self):
        # Arrage
        valid_list = [1,2,3,4,5,6,7,8]

        # Act
        maxOver = maxOverAll(valid_list)

        # Assert
        self.assertEqual(maxOver, 8)

    def test_GIVEN_list_with_one_element_WHEN_compared_THEN_return_that_element(self):
        # Arrage
        valid_list = [1]

        # Act
        maxOver = maxOverAll(valid_list)

        # assert
        self.assertEqual(maxOver, 1)

    def test_GIVEN_empty_list_WHEN_compared_THEN_raise_error(self):

        #Arrage
        empty_list = []

        # assert Act
        with self.assertRaises(ValueError):
            maxOverAll(empty_list)

    def test_GIVEN_list_with_non_numeric_elements_WHEN_compared_THEN_raise_error(self):

        # Arrage
        generic_list = [1,0,-3,2+5j,True,"letter",7,8]

        # Act and Assert
        with self.assertRaises(ValueError):
            maxOverAll(generic_list)

    def test_GIVEN_list_with_all_negative_elements_WHEN_compared_THEN_return_max(self):

        #Arrage
        negative_list = [-1,-2,-3,-4,-5,-6,-7,-8]

        #act
        maxOver = maxOverAll(negative_list)

        #assert
        self.assertEqual(maxOver, -1)


