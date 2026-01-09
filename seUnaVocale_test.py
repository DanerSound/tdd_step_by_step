"""
1. GIVEN_valid_vowel_lowercase_WHEN_checked_THEN_return_true
2. GIVEN_valid_consonant_lowercase_WHEN_checked_THEN_return_false
3. GIVEN_string_with_length_not_equal_to_one_WHEN_checked_THEN_raise_error
4. GIVEN_numeric_character_WHEN_checked_THEN_raise_error
4. GIVEN_non_alphabetic_character_WHEN_checked_THEN_raise_error
"""

import unittest

from seUnaVocale import vowel_checker

class TestVowelChecker(unittest.TestCase):

    def test_GIVEN_valid_vowel_lowercase_WHEN_checked_THEN_return_true(self):
        #arrage
        valid_vowel = 'a'
        #act
        vowel_checker(valid_vowel)
        #assert
        self.assertEqual(vowel_checker(valid_vowel), True)

    def test_GIVEN_valid_consonant_lowercase_WHEN_checked_THEN_return_false(self):
        #arrage
        valid_consonant = 'b'
        #act
        vowel_checker(valid_consonant)
        #assert
        self.assertEqual(vowel_checker(valid_consonant), False)

    def test_string_with_length_not_equal_to_one_WHEN_checked_THEN_raise_error(self):
        # Arrange
        long_string = 'SDFS'

        # Act and Assert
        with self.assertRaises(ValueError):
            vowel_checker(long_string)

    def test_GIVEN_numeric_character_WHEN_checked_THEN_raise_error(self):
        # Arrange
        numeric_character = 123

        # Act and Assert
        with self.assertRaises(TypeError):
            vowel_checker(numeric_character)

    def test_GIVEN_non_alphabetic_character_WHEN_checked_THEN_return_false(self):
        # Arrage
        non_alphabetic_character = "@"

        # Act
        vowel_checker(non_alphabetic_character)

        # assert
        self.assertEqual(vowel_checker(non_alphabetic_character), False)

