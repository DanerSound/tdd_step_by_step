"""
Scrivi una funzione che accetti una lista di dizionari rappresentante una scuola. Ogni dizionario rappresenta uno studente e contiene nome, cognome, classe e voti.
La funzione deve stampare un elenco di tutti gli studenti e calcolare la media dei voti di ciascuno.

------
test_GIVEN_valid_students_with_numeric_grades_WHEN_calculated_THEN_return_students_with_correct_average
test_GIVEN_student_with_boundary_grades_0_and_10_WHEN_calculated_THEN_return_correct_average
test_GIVEN_student_with_float_grades_WHEN_calculated_THEN_return_correct_average

test_GIVEN_student_missing_required_field_WHEN_calculated_THEN_raise_KeyError
test_GIVEN_non_list_students_WHEN_calculated_THEN_raise_TypeError
test_GIVEN_student_with_non_list_grades_WHEN_calculated_THEN_raise_TypeError
test_GIVEN_student_with_empty_grades_list_WHEN_calculated_THEN_return_average_as_None
test_GIVEN_empty_students_list_WHEN_calculated_THEN_return_empty_list
------

test_GIVEN_students_with_string_grades_WHEN_calculated_THEN_raise_TypeError
test_GIVEN_student_with_negative_grade_WHEN_calculated_THEN_raise_ValueError
test_GIVEN_student_with_grade_greater_than_10_WHEN_calculated_THEN_raise_ValueError
test_GIVEN_student_with_mixed_valid_and_invalid_grades_WHEN_calculated_THEN_raise_ValueError

"""

import unittest

from secretary import calculate_student_averages


class TestCalculateStudentAverages(unittest.TestCase):

    def test_GIVEN_valid_students_with_numeric_grades_WHEN_calculated_THEN_return_students_with_correct_average(
        self,
    ):
        students_list = [
            {"nome": "Mario", "cognome": "Rossi", "classe": "3A", "voti": [8, 9, 7]},
            {"nome": "Luigi", "cognome": "Verdi", "classe": "3A", "voti": [6, 7, 8]},
        ]

        result = calculate_student_averages(students_list)

        self.assertEqual(result[0]["media"], 8.0)
        self.assertEqual(result[1]["media"], 7.0)

    def test_GIVEN_student_with_boundary_grades_0_and_10_WHEN_calculated_THEN_return_correct_average(
        self,
    ):
        student_list = [
            {"nome": "Mario", "cognome": "Rossi", "classe": "3A", "voti": [0, 10]},
        ]

        result = calculate_student_averages(student_list)

        self.assertEqual(result[0]["media"], 5.0)

    def test_GIVEN_student_missing_required_field_WHEN_calculated_THEN_raise_KeyError(
        self,
    ):
        students_list = [
            {
                "nome": "Mario",
                "cognome": "Rossi",
                "classe": "3A",
            },  # manca il campo "voti"
        ]

        with self.assertRaises(KeyError):
            calculate_student_averages(students_list)

    def test_GIVEN_non_list_students_WHEN_calculated_THEN_raise_TypeError(
        self,
    ):
        student_list = "not a list"

        with self.assertRaises(TypeError):
            calculate_student_averages(student_list)

    def test_GIVEN_student_with_non_list_grades_WHEN_calculated_THEN_raise_TypeError(
        self,
    ):
        students_list = [
            {"nome": "Mario", "cognome": "Rossi", "classe": "3A", "voti": "Not a list"},
        ]

        with self.assertRaises(TypeError):
            calculate_student_averages(students_list)

    def test_GIVEN_student_with_empty_grades_list_WHEN_calculated_THEN_return_average_as_None(
        self,
    ):
        student_list = [
            {"nome": "Mario", "cognome": "Rossi", "classe": "3A", "voti": []},
        ]

        result = calculate_student_averages(student_list)

        self.assertEqual(result[0]["media"], 0.0)
