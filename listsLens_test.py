"""
Scrivi una funzione che data in ingresso una lista A contenente n parole, restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.

Questo esercizio può essere risolto anche usando una list comprehension.

- test_GIVEN_list_of_strings_WHEN_lengths_calculated_THEN_return_list_of_lengths
- test_GIVEN_list_with_one_string_WHEN_lengths_calculated_THEN_return_single_length
- test_GIVEN_empty_list_WHEN_lengths_calculated_THEN_return_list_with_zero
- test_GIVEN_list_with_non_string_element_WHEN_lengths_calculated_THEN_raise_error

"""

import unittest

from listsLens import listsLens


class TestListsLens(unittest.TestCase):

    def test_GIVEN_list_of_strings_WHEN_lengths_calculated_THEN_return_list_of_lengths(self):

        valid_array=["Ateam","Dragon Ball", "Dragon Ball Z"]

        array_of_lens=listsLens(valid_array)

        self.assertEqual(array_of_lens, [5, 11, 13])

    def test_GIVEN_list_with_one_string_WHEN_lengths_calculated_THEN_return_single_length(self):

        valid_array=["Ateam"]

        array_of_lens=listsLens(valid_array)

        self.assertEqual(array_of_lens, [5])

    def test_GIVEN_empty_list_WHEN_lengths_calculated_THEN_return_list_with_zero(self):

        empty_array=[]

        array_of_lens=listsLens(empty_array)

        self.assertEqual(array_of_lens, [0])

    def test_GIVEN_list_with_non_string_element_WHEN_lengths_calculated_THEN_raise_error(self):
        generic_list = ["Ateam", 1, 0, -3, 2 + 5j, True, "letter", 7.3, 8]

        with self.assertRaises(TypeError):
            listsLens(generic_list)



