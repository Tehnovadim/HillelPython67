import sqlite3
from pprint import pprint

DB_PATH = 'school_db.sqlite3'

with sqlite3.connect(DB_PATH) as connection:
    cursor = connection.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS schools(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            school_number INTEGER NOT NULL,
            address TEXT NOT NULL,
            floors INTEGER NOT NULL CHECK (floors >= 1)
        )
    """
    cursor.execute(query)

    query = """
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            last_name TEXT NOT NULL,
            first_name TEXT NOT NULL,
            specialization TEXT NOT NULL,
            school_id INTEGER,
            FOREIGN KEY (school_id) REFERENCES schools(id)
        )
    """
    cursor.execute(query)

    query = """
        INSERT INTO schools(school_number, address, floors)
        VALUES (?, ?, ?)
    """
    cursor.execute(query, (1, '123 Main St', 3))
    cursor.execute(query, (2, '456 Oak St', 4))
    cursor.execute(query, (3, '789 Pine St', 2))

    students = [
        ('Ivanov', 'Ivan', 'Mathematics', 1),
        ('Petrov', 'Petr', 'Physics', 2),
        ('Sidorov', 'Sidr', 'Biology', 3),
        ('Kuznetsova', 'Maria', 'Mathematics', 1),
        ('Popova', 'Anna', 'Chemistry', 2),
        ('Smirnov', 'Alexey', 'Physics', 3),
        ('Kozlov', 'Nikolay', 'Literature', 1),
        ('Sokolova', 'Elena', 'History', 2),
        ('Volkov', 'Dmitry', 'Geography', 3),
        ('Orlova', 'Irina', 'Art', 1)
    ]
    query = """
        INSERT INTO students(last_name, first_name, specialization, school_id)
        VALUES (?, ?, ?, ?)
    """
    cursor.executemany(query, students)

    query = """
        SELECT students.last_name, students.first_name, students.specialization, schools.school_number
        FROM students
        JOIN schools ON students.school_id = schools.id
    """
    result = cursor.execute(query)
    pprint(result.fetchall(), width=40)
