"""
Esercizio 008
Generatore di Istogrammi
Scrivi una semplice funzione che, data una lista di numeri, fornisca in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.

Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:

***

*******

*********

*****

test_GIVEN_list_of_positive_integers_WHEN_histogram_generated_THEN_return_correct_histogram
test_GIVEN_list_with_one_element_WHEN_histogram_generated_THEN_return_single_row
test_GIVEN_empty_list_WHEN_histogram_generated_THEN_raise_error
test_GIVEN_list_with_non_integer_element_WHEN_histogram_generated_THEN_raise_error
test_GIVEN_list_with_negative_integer_WHEN_histogram_generated_THEN_raise_error
test_GIVEN_list_with_zero_WHEN_histogram_generated_THEN_return_empty_row

"""

import unittest

from istogramGenerartor import istogramGenerartor

class TestIstogramGenerator(unittest.TestCase):

    def test_GIVEN_list_of_positive_integers_WHEN_histogram_generated_THEN_return_correct_histogram(self):

        valid_list = [3, 7, 9, 5]

        valid_istogram = istogramGenerartor(valid_list)

        expected_istogram = [ "***", "*******","*********","*****"]

        self.assertEqual(valid_istogram, expected_istogram)

    def test_GIVEN_list_with_one_element_WHEN_histogram_generated_THEN_return_single_row(self):
        valid_list = [3]

        valid_istogram = istogramGenerartor(valid_list)

        expected_istogram = [ "***"]

        self.assertEqual(valid_istogram, expected_istogram)

    def test_GIVEN_empty_list_WHEN_histogram_generated_THEN_raise_error(self):
        empty_list = []

        with self.assertRaises(ValueError):
            istogramGenerartor(empty_list)

    def test_GIVEN_list_with_non_integer_element_WHEN_histogram_generated_THEN_raise_error(self):

        generic_list = [3, 7, 9, 5.2]

        with self.assertRaises(ValueError):
            istogramGenerartor(generic_list)

    def test_GIVEN_list_with_negative_integer_WHEN_histogram_generated_THEN_raise_error(self):

        generic_list = [-3, 7, 9.4, 5]

        with self.assertRaises(ValueError):
            istogramGenerartor(generic_list)

    def test_GIVEN_list_with_zero_WHEN_histogram_generated_THEN_return_empty_row(self):

        valid_list = [3, 0, 9, 5]

        istogram = istogramGenerartor(valid_list)

        expected_istogram = [ "***", "", "*********", "*****"]

        self.assertEqual(expected_istogram, istogram)