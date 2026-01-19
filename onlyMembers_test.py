import unittest

from onlyMembers import memberCheck

"""
test_GIVEN_element_present_in_list_WHEN_searched_THEN_return_index
test_GIVEN_element_not_present_in_list_WHEN_searched_THEN_return_not_present_message
test_GIVEN_list_with_duplicate_elements_WHEN_searched_THEN_return_first_index
test_GIVEN_empty_list_WHEN_searched_THEN_raise_error
test_GIVEN_search_element_is_empty_string_WHEN_searched_THEN_raise_error
"""

class Test(unittest.TestCase):

    def test_GIVEN_element_present_in_list_WHEN_searched_THEN_return_index(self):

        #arrange
        to_check =  2
        team_list = ["team1", 2, "A_team", 1, 3.5 ]

        #act
        result = memberCheck(to_check, team_list)

        #assert
        self.assertEqual(result, 1)

    def test_GIVEN_element_not_present_in_list_WHEN_searched_THEN_return_not_present_message(self):

        to_check = "A_team"
        team_list = ["team1", 2, "B_team", 1, 3.5 ]

        result = memberCheck(to_check, team_list)

        self.assertEqual(result, "element not present")

    def test_GIVEN_list_with_duplicate_elements_WHEN_searched_THEN_return_first_index(self):

        to_check = "A_team"
        team_list = ["team1", 2, "A_team","A_team", 3.5 ]

        result = memberCheck(to_check, team_list)

        self.assertEqual(result, 2)

    def test_GIVEN_empty_list_WHEN_searched_THEN_raise_error(self):

        to_check = "A_team"
        team_list = []

        with self.assertRaises(ValueError):
            memberCheck(to_check, team_list)

    def test_GIVEN_search_element_is_empty_string_WHEN_searched_THEN_raise_error(self):

        to_check = ""
        team_list = ["team1", 2, "A_team", 1, 3.5]

        with self.assertRaises(ValueError):
            memberCheck(to_check, team_list)
