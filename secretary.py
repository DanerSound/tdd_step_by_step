
def student_validator(student):
    required_fields = ['nome', 'cognome', 'classe', 'voti']
    for field in required_fields:
        if field not in student:
            raise KeyError(f"Missing required field: {field}")
        
    if not isinstance(student['voti'], list):
            raise TypeError("Grades must be a list")



def calculate_student_averages(students_list):
    if not isinstance(students_list, list):
        raise TypeError("Input must be a list of students")
    
    for student in students_list:
        student_validator(student)

    return None