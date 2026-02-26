import unittest

from continuesPrint import string_joiner

"""
Scrivi una funzione che prenda una serie di input dall'utente utilizzando un ciclo while e li stampi con la funzione print senza andare a capo. Il ciclo while si deve interrompere quando l'utente preme INVIO senza scrivere nulla.

test_GIVEN_non_empty_strings_ending_with_empty_WHEN_concatenated_THEN_return_joined_string

test_GIVEN_empty_string_as_first_input_WHEN_concatenated_THEN_return_empty_string

test_GIVEN_empty_string_in_middle_WHEN_concatenated_THEN_stop_and_return_partial_string

test_GIVEN_only_one_non_empty_string_followed_by_empty_WHEN_concatenated_THEN_return_that_string

test_GIVEN_multiple_non_empty_strings_without_empty_WHEN_concatenated_THEN_return_full_joined_string

test_GIVEN_strings_containing_spaces_WHEN_concatenated_THEN_preserve_spaces

test_GIVEN_strings_containing_tab_character_WHEN_concatenated_THEN_preserve_tab_character
"""

class TestContinuesPrint(unittest.TestCase):

    def test_GIVEN_non_empty_strings_ending_with_empty_WHEN_concatenated_THEN_return_joined_string(self):

        current = "a b c d e f g"
        last_char = ''

        joinedString = string_joiner(current, last_char)

        self.assertEqual(joinedString, "a b c d e f g ")

    def test_GIVEN_empty_string_as_first_input_WHEN_concatenated_THEN_return_empty_string(self):
        current = ""
        last_char = ''

        joinedString = string_joiner(current, last_char)

        self.assertEqual(joinedString, " ")

    def test_GIVEN_empty_string_in_middle_WHEN_concatenated_THEN_stop_and_return_partial_string(self):
        current = "a b c"
        last_char = ''

        joinedString = string_joiner(current, last_char)

        self.assertEqual(joinedString, "a b c ")

    def test_GIVEN_only_one_non_empty_string_followed_by_empty_WHEN_concatenated_THEN_return_that_string(self):
        current = "a "
        last_char = ''

        joinedString = string_joiner(current, last_char)

        self.assertEqual(joinedString, "a  ")

    def test_GIVEN_strings_containing_spaces_WHEN_concatenated_THEN_preserve_spaces(self):
        current = "   "
        last_char = ''

        joinedString = string_joiner(current, last_char)

        self.assertEqual(joinedString, "    ")

    def test_GIVEN_strings_containing_tab_character_WHEN_concatenated_THEN_preserve_tab_character(self):
        current = "a    "
        last_char = ''

        joinedString = string_joiner(current, last_char)

        self.assertEqual(joinedString, "a     ")