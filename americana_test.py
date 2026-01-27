"""
Scrivi una funzione che, dato in ingresso un valore espresso in metri, mandi in print l'equivalente in miglia terrestri, iarde, piedi e pollici. Come risolverai questo esercizio?

test_GIVEN_valid_meters_WHEN_converted_THEN_return_correct_conversions
test_GIVEN_invalid_meters_WHEN_converted_THEN_raises_error
test_GIVEN_zero_meters_WHEN_converted_THEN_return_all_zero_values
test_GIVEN_negative_meters_WHEN_converted_THEN_raise_error
test_GIVEN_non_numeric_input_WHEN_converted_THEN_raise_error

"""
import unittest
from americana import toamericanunit


class TestAmericana(unittest.TestCase):

    def test_GIVEN_valid_meters_WHEN_converted_THEN_return_correct_conversions(self):

        valid_meters = 5

        collection_units=toamericanunit(valid_meters)

        expected_units ={
            "feet": valid_meters*3.28084,
            "yards": valid_meters*1.09361,
            "miles": valid_meters*0.000621371,
        }

        self.assertEqual(collection_units, expected_units)

    def test_GIVEN_invalid_meters_WHEN_converted_THEN_raises_error(self):

        invalid_meters = "test"

        with self.assertRaises(ValueError):
            toamericanunit(invalid_meters)

    def test_GIVEN_zero_meters_WHEN_converted_THEN_return_all_zero_values(self):

        zero_meters = 0

        collection_units=toamericanunit(zero_meters)

        expected_units = {
            "feet": zero_meters * 3.28084,
            "yards": zero_meters * 1.09361,
            "miles": zero_meters * 0.000621371,
        }

        self.assertEqual(collection_units, expected_units)

    def test_GIVEN_negative_meters_WHEN_converted_THEN_raise_error(self):

        negative_meters = -4

        with self.assertRaises(ValueError):
            toamericanunit(negative_meters)

    def test_GIVEN_non_numeric_input_WHEN_converted_THEN_raise_error(self):
        numeric_input = "1"

        with self.assertRaises(ValueError):
            toamericanunit(numeric_input)

