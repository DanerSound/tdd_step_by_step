def validate_students(students: list[dict]) -> None:
    if not isinstance(students, list):
        raise TypeError("students must be a list")

    required_fields = {"nome", "cognome", "classe", "voti"}

    for student in students:
        if not isinstance(student, dict):
            raise TypeError("each student must be a dictionary")

        missing = required_fields - student.keys()
        if missing:
            raise KeyError(f"missing fields: {missing}")

        grades = student["voti"]

        if not isinstance(grades, list):
            raise TypeError("voti must be a list")

        for grade in grades:
            if not isinstance(grade, (int, float)):
                raise TypeError("grades must be numeric")

            if not 0 <= grade <= 10:
                raise ValueError("grades must be between 0 and 10")


def calculate_student_averages(students: list[dict]) -> list[dict]:
    if not students:
        return []

    validate_students(students)

    result = []

    for student in students:
        grades = student["voti"]

        if not grades:
            avg = None
        else:
            avg = sum(grades) / len(grades)

        result.append(
            {"nome": student["nome"], "cognome": student["cognome"], "media": avg}
        )

    return result
