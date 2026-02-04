"""
Funzione Genera MAC
Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, a un chipset per comunicazioni wireless (es WiFi o Bluetooth), composto da 6 coppie di cifre esadecimali separate da due punti.

Un esempio di MAC è 02:FF:A5:F2:55:12.

Scrivi una funzione genera_mac() che generi degli indirizzi MAC pseudo casuali utilizzando il modulo random.

test_GIVEN_no_input_WHEN_mac_generated_THEN_return_string
test_GIVEN_generated_mac_WHEN_split_by_colon_THEN_have_six_groups
test_GIVEN_generated_mac_WHEN_groups_checked_THEN_each_group_has_length_two
test_GIVEN_generated_mac_WHEN_characters_checked_THEN_only_hexadecimal_chars_used
test_GIVEN_generated_mac_WHEN_format_checked_THEN_use_colon_as_separator
test_GIVEN_generated_mac_WHEN_length_checked_THEN_length_is_seventeen

"""
import unittest
import re

from macGenerartor import mac_generator


class TestMACGenerator(unittest.TestCase):

    def test_GIVEN_no_input_WHEN_mac_generated_THEN_return_string(self):
        valid_mac = mac_generator()

        self.assertEqual(type(valid_mac), type('02:FF:A5:F2:55:12'))

    def test_GIVEN_generated_mac_WHEN_split_by_colon_THEN_have_six_groups(self):
        valid_mac = mac_generator()

        mac_length = valid_mac.split(':')

        self.assertEqual(len(mac_length), 6)

    def test_GIVEN_generated_mac_WHEN_groups_checked_THEN_each_group_has_length_two(self):
        valid_mac = mac_generator()

        mac_length = valid_mac.split(':')

        self.assertEqual(len(mac_length[0]), 2)

    def test_GIVEN_generated_mac_WHEN_characters_checked_THEN_only_hexadecimal_chars_used(self):
        mac_address = mac_generator()
        characters = mac_address.replace(":", "")

        for char in characters:
            self.assertTrue(
                char.isdigit() or char.upper() in ["A", "B", "C", "D", "E", "F"],
                msg=f"Invalid hex character found: {char}"
            )

    def test_GIVEN_generated_mac_WHEN_format_checked_THEN_use_colon_as_separator(self):
        mac_address = mac_generator()
        mac_list = mac_address.split(':')

        self.assertEqual(len(mac_list), 6)
        self.assertEqual(mac_address.count(':'), 5)

    def test_GIVEN_generated_mac_WHEN_length_checked_THEN_length_is_seventeen(self):
        mac_address = mac_generator()

        self.assertEqual(len(mac_address), 17)
