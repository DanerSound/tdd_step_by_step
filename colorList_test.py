"""
Scrivi una funzione che aggiunga ad una lista 10 colori inseriti dall'utente. Il programma deve poi chiedere all'utente di inserire una lettera e mostrare in output solo i colori nella lista che iniziano con quella lettera.

test_GIVEN_color_list_and_valid_letter_WHEN_filtered_THEN_return_matching_colors
test_GIVEN_no_matching_colors_WHEN_filtered_THEN_return_empty_list
test_GIVEN_empty_color_list_WHEN_filtered_THEN_return_empty_list

test_GIVEN_non_string_letter_WHEN_filtered_THEN_raise_TypeError
test_GIVEN_letter_with_length_not_1_WHEN_filtered_THEN_raise_ValueError
test_GIVEN_non_alphabetic_letter_WHEN_filtered_THEN_raise_ValueError

test_GIVEN_uppercase_letter_WHEN_filtered_THEN_handle_case_correctly
test_GIVEN_color_list_with_non_string_element_WHEN_filtered_THEN_raise_TypeError

"""
import unittest
from colorList import find_color


class TestColorList(unittest.TestCase):

    def test_GIVEN_color_list_and_valid_letter_WHEN_filtered_THEN_return_matching_colors(self):

        color_list = ["red", "green", "blue", "yellow", "magenta", "cyan", "white"]

        letter = 'y'

        list_of_colors = find_color(color_list, letter)

        self.assertEqual(list_of_colors, ["yellow"])

    def test_GIVEN_no_matching_colors_WHEN_filtered_THEN_return_empty_list(self):
        color_list = ["red", "green", "blue", "yellow", "magenta", "cyan", "white"]

        letter = 'x'

        list_of_colors = find_color(color_list, letter)

        self.assertNotEqual(list_of_colors, [""])

    def test_GIVEN_empty_color_list_WHEN_filtered_THEN_return_empty_list(self):
        color_list = [""]

        letter = 'x'

        list_of_colors = find_color(color_list, letter)

        self.assertNotEqual(list_of_colors, [""])

    def test_GIVEN_non_string_letter_WHEN_filtered_THEN_raise_TypeError(self):
        color_list = ["red", "green", "blue", "yellow", "magenta", "cyan", "white"]

        letter = 1

        with self.assertRaises(TypeError):
            find_color(color_list, letter)

    def test_GIVEN_letter_with_length_not_1_WHEN_filtered_THEN_raise_ValueError(self):
        color_list = ["red", "green", "blue", "yellow", "magenta", "cyan", "white"]

        letter = 'ab'

        with self.assertRaises(ValueError):
            find_color(color_list, letter)

    def test_GIVEN_non_alphabetic_letter_WHEN_filtered_THEN_raise_ValueError(self):

        color_list = ["red", "green", "blue", "yellow", "magenta", "cyan", "white"]

        letter = '!'

        with self.assertRaises(ValueError):
            find_color(color_list, letter)

    def test_GIVEN_uppercase_letter_WHEN_filtered_THEN_handle_case_correctly(self):
        color_list = ["red", "green", "blue", "yellow", "magenta", "cyan", "white"]

        letter = 'Y'

        list_of_colors = find_color(color_list, letter)

        self.assertEqual(list_of_colors, ["yellow"])

    def test_GIVEN_color_list_with_non_string_element_WHEN_filtered_THEN_raise_TypeError(self):
        color_list = ["red", "green", 42, "blue"]
        letter = "r"

        with self.assertRaises(TypeError):
            find_color(color_list, letter)


