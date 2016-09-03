# Student becomes the teacher exercise：
"""
Build functions to get the average score/letter grade for single student and the whole class
"""
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}


def average(numbers):  # Calculate the average score
    total = float(sum(numbers))
    return total / len(numbers)


def get_average(student):  # Calculate the weighted average score
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return homework * 0.1 + quizzes * 0.3 + tests * 0.6


def get_letter_grade(score):  # Return the letter grade according to the score
    if score >= 90:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

print(get_letter_grade(lloyd))


def get_class_average(all_students):  # Average score in the class
    results = []
    for student in all_students:
        results.append(get_average(student))  # Remember don't assign the value when using append!
    return average(results)  # Return should be in the same line as for-loop


students = [lloyd, alice, tyler]
print(get_class_average(students))
print(get_letter_grade(get_class_average(students)))  # Average letter grade
