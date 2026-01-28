"""
Scrivi una semplice funzione che converta un dato numero di giorni, ore e minuti, passati dall'utente tramite funzione input, in secondi.

GIVEN_days_hours_minutes_all_positive_WHEN_convert_THEN_return_correct_seconds
GIVEN_all_values_zero_WHEN_convert_THEN_return_zero
GIVEN_some_values_zero_WHEN_convert_THEN_return_correct_seconds
GIVEN_negative_values_WHEN_convert_THEN_raise_error
"""

import unittest

from timeContoller import time_controller

class TestTimeController(unittest.TestCase):

    def test_GIVEN_days_hours_minutes_all_positive_WHEN_convert_THEN_return_correct_seconds(self):
        days="2"
        hours="2"
        minutes="2"

        result=time_controller(int(days), int(hours), int(minutes))

        self.assertEqual(result,int(days) * 86400 + int(hours) * 3600 + int(minutes) * 60)

    def test_GIVEN_all_values_zero_WHEN_convert_THEN_return_zero(self):
        days="0"
        hours="0"
        minutes="0"

        result=time_controller(int(days), int(hours), int(minutes))

        self.assertEqual(result, int(days) * 86400 + int(hours) * 3600 + int(minutes) * 60)

    def test_GIVEN_some_values_zero_WHEN_convert_THEN_return_correct_seconds(self):
        days="0"
        hours="2"
        minutes="1"

        result=time_controller(int(days), int(hours), int(minutes))

        self.assertEqual(result, int(days) * 86400 + int(hours) * 3600 + int(minutes) * 60)

    def test_GIVEN_negative_values_WHEN_convert_THEN_raise_error(self):
        days="1"
        hours="-2"
        minutes="50"

        with self.assertRaises(ValueError):
            time_controller(int(days), int(hours), int(minutes))
