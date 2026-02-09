"""
Scrivi una funzione che, dato un carattere in ingresso, restituisca in output il codice ASCII associato al carattere passato.

Anche in questo caso, usare una libreria potrebbe facilitare la risoluzione dell'esercizio!

test_GIVEN_printable_ascii_character_WHEN_converted_THEN_return_ascii_code
test_GIVEN_space_character_WHEN_converted_THEN_return_ascii_code
test_GIVEN_non_printable_character_WHEN_converted_THEN_raise_error
test_GIVEN_string_with_length_not_equal_one_WHEN_converted_THEN_raise_error
test_GIVEN_none_input_WHEN_converted_THEN_raise_error
test_GIVEN_non_string_input_WHEN_converted_THEN_raise_error
test_GIVEN_non_ascii_character_WHEN_converted_THEN_raise_error
"""

import unittest
from findAscii import custom_ascii
class TestFindAscii(unittest.TestCase):

    def test_GIVEN_printable_ascii_character_WHEN_converted_THEN_return_ascii_code(self):
        printable = 'A'

        ascii_code = custom_ascii(printable)

        self.assertEqual(ascii_code, ord(printable))

    def test_GIVEN_space_character_WHEN_converted_THEN_return_ascii_code(self):
        printable = ' '

        ascii_code = custom_ascii(printable)

        self.assertEqual(ascii_code, ord(printable))

    def test_GIVEN_string_with_length_not_equal_one_WHEN_converted_THEN_raise_error(self):
        not_printable = 'aa'

        with self.assertRaises(ValueError):
            custom_ascii(not_printable)

    def test_GIVEN_none_input_WHEN_converted_THEN_raise_error(self):
        not_printable = None

        with self.assertRaises(TypeError):
            custom_ascii(not_printable)

    def test_GIVEN_non_string_input_WHEN_converted_THEN_raise_error(self):
        not_a_string = 65

        with self.assertRaises(TypeError):
            custom_ascii(not_a_string)

    def test_GIVEN_non_ascii_character_WHEN_converted_THEN_raise_error(self):
        non_ascii_char = 'é'  # Unicode, fuori ASCII

        with self.assertRaises(ValueError):
            custom_ascii(non_ascii_char)