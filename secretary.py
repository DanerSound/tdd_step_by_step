
def student_validator(student):
    required_fields = ['nome', 'cognome', 'classe', 'voti']
    for field in required_fields:
        if field not in student:
            raise KeyError(f"Missing required field: {field}")



def calculate_student_averages(students_list):
    for student in students_list:
        student_validator(student)

    return None