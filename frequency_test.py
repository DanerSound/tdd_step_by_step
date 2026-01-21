"""
Scrivi una funzione che, data una stringa come parametro, restituisca un dizionario rappresentante la "frequenza di comparsa" di ciascun carattere componente la stringa.

Per fare un esempio, data una stringa "ababcc", otterremo in risultato {"a": 2, "b": 2, "c": 2}

test_GIVEN_valid_string_WHEN_frequency_calculated_THEN_return_correct_dictionary
test_GIVEN_string_with_repeated_characters_WHEN_frequency_calculated_THEN_count_correctly
test_GIVEN_empty_string_WHEN_frequency_calculated_THEN_return_empty_dictionary
test_GIVEN_string_with_spaces_WHEN_frequency_calculated_THEN_count_spaces
test_GIVEN_non_string_input_WHEN_frequency_calculated_THEN_raise_error

"""

import unittest

from frequency import frequency_letters

class TestFrequency(unittest.TestCase):

    def test_GIVEN_valid_string_WHEN_frequency_calculated_THEN_return_correct_dictionary(self):
        valid_string = "ababcc"

        freq_dict = frequency_letters(valid_string)

        self.assertEqual(freq_dict, {"a": 2, "b": 2, "c": 2})

    def test_GIVEN_string_with_repeated_characters_WHEN_frequency_calculated_THEN_count_correctly(self):
        valid_string = "aababcc"

        freq_dict = frequency_letters(valid_string)

        self.assertEqual(freq_dict, {"a": 3, "b": 2, "c": 2})

    def test_GIVEN_empty_string_WHEN_frequency_calculated_THEN_return_empty_dictionary(self):
        valid_string = ""

        freq_dict = frequency_letters(valid_string)

        self.assertEqual(freq_dict, {})

    def test_GIVEN_string_with_spaces_WHEN_frequency_calculated_THEN_count_spaces(self):
        valid_string = "a ab ab cc"

        freq_dict = frequency_letters(valid_string)

        self.assertEqual(freq_dict, {"a": 3," ": 3,"b": 2, "c": 2})

    def test_GIVEN_non_string_input_WHEN_frequency_calculated_THEN_raise_error(self):

        invalid_input = 1

        with self.assertRaises(TypeError):
            frequency_letters(invalid_input)


