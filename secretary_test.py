"""
Scrivi una funzione che accetti una lista di dizionari rappresentante una scuola. Ogni dizionario rappresenta uno studente e contiene nome, cognome, classe e voti. La funzione deve stampare un elenco di tutti gli studenti e calcolare la media dei voti di ciascuno.

qui ci sono diversi aspetti da considerare la funzione da scrivere deve essere in grado di gestire casi in cui alcuni studenti non hanno voti,

o quando i voti sono rappresentati come stringhe invece che numeri. Inoltre, la funzione dovrebbe essere in grado di gestire casi in cui la lista di studenti è vuota. 

(che vuol dire che non ci sono studenti inseriti in quella classe) o quando ci sono studenti con voti non validi (ad esempio, voti negativi o superiori a 10).
------
test_GIVEN_student_missing_required_field_WHEN_calculated_THEN_raise_KeyError
test_GIVEN_non_list_students_WHEN_calculated_THEN_raise_TypeError
test_GIVEN_student_with_non_list_grades_WHEN_calculated_THEN_raise_TypeError
------
test_GIVEN_valid_students_with_numeric_grades_WHEN_calculated_THEN_return_students_with_correct_average
test_GIVEN_student_with_empty_grades_list_WHEN_calculated_THEN_return_average_as_None
test_GIVEN_empty_students_list_WHEN_calculated_THEN_return_empty_list
test_GIVEN_students_with_string_grades_WHEN_calculated_THEN_raise_TypeError
test_GIVEN_student_with_negative_grade_WHEN_calculated_THEN_raise_ValueError
test_GIVEN_student_with_grade_greater_than_10_WHEN_calculated_THEN_raise_ValueError
test_GIVEN_student_with_mixed_valid_and_invalid_grades_WHEN_calculated_THEN_raise_ValueError
test_GIVEN_student_with_boundary_grades_0_and_10_WHEN_calculated_THEN_return_correct_average
test_GIVEN_student_with_float_grades_WHEN_calculated_THEN_return_correct_average
"""

import unittest

from secretary import calculate_student_averages

class TestCalculateStudentAverages(unittest.TestCase):
    def test_GIVEN_student_missing_required_field_WHEN_calculated_THEN_raise_KeyError(self):
        students_list = [
            {"nome": "Mario", "cognome": "Rossi", "classe": "3A"},  # manca il campo "voti"
        ]

        with self.assertRaises(KeyError):
            calculate_student_averages(students_list)

