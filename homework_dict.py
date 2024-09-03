import random

students = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}

new_student = {
    'Пошта': 'Olexa@gmail.com',
    'Вік': random.randint(18, 40),
    'Номер телефону': '+380987654321',
    'Середній бал': random.uniform(0, 100)
}

students['Олексій Довженко'] = new_student
print(f"Додано нового студента: Олексій Довженко з середнім балом {new_student['Середній бал']}.\n")

high_achievers = {name: info['Середній бал'] for name, info in students.items() if info['Середній бал'] > 90}
print("Студенти із середнім балом більше 90:")
for name, grade in high_achievers.items():
    print(f"{name}: Середній бал = {grade}")

print()

average_grade = sum(student['Середній бал'] for student in students.values()) / len(students)
print(f"Середній бал по групі: {average_grade:.2f}\n")

parent_phone = '+380999999999'
for name, info in students.items():
    if not info['Номер телефону']:
        info['Номер телефону'] = parent_phone
        print(f"У студента {name} не було номера телефону, записано номер батьків: {parent_phone}")

print("\nОновлений список студентів:")
for name, info in students.items():
    print(f"{name}: {info}")
