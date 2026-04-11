"""
Scrivi una funzione che permetta di inserire una canzone e salvarla in un file di testo. Il programma deve chiedere all'utente di inserire il titolo e il testo della canzone, e poi salvare quest'ultimo in un file intitolato titolo_canzone.txt.

Suggerimento: dovrai utilizzare l'istruzione with.

test_GIVEN_valid_title_and_text_WHEN_saved_THEN_file_is_created_with_correct_name
test_GIVEN_empty_title_WHEN_validated_THEN_raise_ValueError
test_GIVEN_empty_text_WHEN_validated_THEN_raise_ValueError
test_GIVEN_title_with_only_spaces_WHEN_validated_THEN_raise_ValueError
test_GIVEN_title_with_spaces_WHEN_filename_built_THEN_spaces_replaced_with_underscore
test_GIVEN_title_with_uppercase_WHEN_filename_built_THEN_lowercase_filename
test_GIVEN_title_with_special_characters_WHEN_filename_built_THEN_sanitized_filename
"""

import unittest

from songRegister import songValidator


class TestSongRegister(unittest.TestCase):

    def test_GIVEN_valid_title_and_text_WHEN_saved_THEN_file_is_created_with_correct_name(
            self,
    ):
        song_title = "My Song Title"

        song_text = "My song text"

        valid = songValidator(song_title, song_text)

        self.assertTrue(valid)