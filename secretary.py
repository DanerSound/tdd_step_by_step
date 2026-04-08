def student_validator(students_list):
    if not isinstance(students_list, list):
        raise TypeError("Input must be a list of students")

    required_fields = ["nome", "cognome", "classe", "voti"]

    for student in students_list:
        for field in required_fields:
            if field not in student:
                raise KeyError(f"Missing required field: {field} in student: {student}")

    if not isinstance(student["voti"], list):
        raise TypeError("Grades must be a list")


def calculate_student_averages(students_list):
    if len(students_list) == 0:
        return []
    student_validator(students_list)
    student_avg = []
    media = 0
    for student in students_list:
        if len(student["voti"]) == 0:
            student_avg.append(
                {"nome": student["nome"], "cognome": student["cognome"], "media": 0.0}
            )
        else:
            media = sum(student["voti"]) / len(student["voti"])
            student_avg.append(
                {"nome": student["nome"], "cognome": student["cognome"], "media": media}
            )
    return student_avg
