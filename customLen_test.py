
import unittest
from customLen import customLen


"""
Scrivi una funzione che restituisca la lunghezza di una stringa o lista passata come parametro. In sostanza, seppur presente, provate a scrivere la nostra versione della funzione len!
    
    test_GIVEN_valid_string_WHEN_length_calculated_THEN_return_length
    test_GIVEN_valid_list_WHEN_length_calculated_THEN_return_length
    test_GIVEN_empty_input_WHEN_length_calculated_THEN_return_zero
    
    test_GIVEN_non_iterable_input_WHEN_length_calculated_THEN_raise_error
    
    test_GIVEN_list_with_mixed_elements_WHEN_length_calculated_THEN_return_length
    test_GIVEN_string_with_spaces_WHEN_length_calculated_THEN_count_spaces
    test_GIVEN_none_input_WHEN_length_calculated_THEN_raise_error

"""
class TestCustomLen(unittest.TestCase):

    def test_GIVEN_valid_string_WHEN_length_calculated_THEN_return_length(self):

        valid_string = "Hello World"

        string_length = customLen(valid_string)

        self.assertEqual(string_length, len(valid_string))

    def test_GIVEN_valid_list_WHEN_length_calculated_THEN_return_length(self):

        valid_list = [1, 2, 3]

        list_length = customLen(valid_list)

        self.assertEqual(list_length, len(valid_list))

    def test_GIVEN_empty_input_WHEN_length_calculated_THEN_return_zero(self):

        # empty_input = ""
        empty_input_list = []

        object_length = customLen(empty_input_list)

        self.assertEqual(object_length, 0)

    def test_GIVEN_list_with_mixed_elements_WHEN_length_calculated_THEN_return_length(self):

        generic_array = [1, 0, -3, 2 + 5j, True, "letter", 7.3, 8]

        generic_array_length = customLen(generic_array)

        self.assertEqual(generic_array_length, len(generic_array))

    def test_GIVEN_string_with_spaces_WHEN_length_calculated_THEN_count_spaces(self):
        valid_string = "H e l l o World"

        string_length = customLen(valid_string)

        self.assertEqual(string_length, len(valid_string))

    def test_GIVEN_non_iterable_input_WHEN_length_calculated_THEN_raise_error(self):
        not_iterable_list = 1

        with self.assertRaises(TypeError):
            customLen(not_iterable_list)