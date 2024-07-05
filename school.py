student_grades_9a = {
    "Олександр Іванович Петров": 85,
    "Марія Сергіївна Іванова": 90,
    "Дмитро Олександрович Сидоров": 78
}

student_grades_9b = {
    "Катерина Петрівна Коваленко": 88,
    "Іван Дмитрович Кузьменко": 92,
    "Ольга Вікторівна Литвиненко": 80
}

student_grades_9 = {
    "9A": student_grades_9a,
    "9B": student_grades_9b
}

for class_name, students in student_grades_9.items():
    print(f"Клас {class_name}:")
    for student, grade in students.items():
        print(f"  {student}: {grade}")
    print()