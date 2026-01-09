import unittest

from ultraSum import custom_sum

"""
Scrivi un semplice programma che, data una lista di numeri, sommi tra loro tutti gli elementi.
Suggerimento: anche se esiste la funzione sum() per risolvere l'esercizio potresti usare il ciclo for.

1. GIVEN_list_of_valid_numbers_WHEN_summed_THEN_return_sum
2. GIVEN_list_with_one_element_WHEN_summed_THEN_return_that_element
3. GIVEN_empty_list_WHEN_summed_THEN_raise_error
4. GIVEN_list_with_non_summable_element_WHEN_summed_THEN_raise_error

"""

class TestUltraSum(unittest.TestCase):

    def test_GIVEN_list_of_valid_numbers_WHEN_summed_THEN_return_sum(self):
        # arrange
        valid_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

        # act
        sum_of_valid_numbers = custom_sum(valid_numbers)

        # assert
        self.assertEqual(sum_of_valid_numbers, 120)

    def test_GIVEN_list_with_one_element_WHEN_summed_THEN_return_that_element(self):

        #arrange
        one_el_list = [1]
        #act
        sum_of_one_el_list = custom_sum(one_el_list)
        #assert
        self.assertEqual(sum_of_one_el_list, 1)

    def test_GIVEN_empty_list_WHEN_summed_THEN_raise_error(self):

        #arrange
        empty_list = []

        with self.assertRaises(TypeError):
            custom_sum(empty_list)

    def test_GIVEN_list_with_non_summable_element_WHEN_summed_THEN_raise_error(self):

        generic_array = [1,0,-3,2+5j,True,"letter",7,8]

        with self.assertRaises(ValueError):
            custom_sum(generic_array)