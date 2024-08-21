import sqlite3
from pprint import pprint

DB_PATH = 'school.db'

with sqlite3.connect(DB_PATH) as connection:
    cursor = connection.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS schools (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            school_number INTEGER NOT NULL,
            address TEXT NOT NULL,
            number_of_floors INTEGER NOT NULL CHECK (number_of_floors > 0)
        )
    """
    cursor.execute(query)

    query = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            last_name TEXT NOT NULL,
            first_name TEXT NOT NULL,
            specialization TEXT,
            school_id INTEGER,
            phone_number TEXT,
            FOREIGN KEY (school_id) REFERENCES schools(id)
        )
    """
    cursor.execute(query)

    schools = [
        (1, '123 Main St', 3),
        (2, '456 Oak Ave', 2),
        (3, '789 Pine Rd', 4),
    ]
    query = """
        INSERT INTO schools(school_number, address, number_of_floors)
        VALUES (?, ?, ?)
    """
    cursor.executemany(query, schools)

    students = [
        ('Smith', 'John', 'Mathematics', 1),
        ('Doe', 'Jane', 'Physics', 2),
        ('Brown', 'Charlie', 'Biology', 3),
        ('Taylor', 'Ann', 'Chemistry', 1),
        ('Johnson', 'Emily', 'Literature', 2),
        ('White', 'Chris', 'Art', 3),
        ('Martin', 'Sam', 'Music', 1),
        ('Lee', 'Alex', 'Computer Science', 2),
        ('Walker', 'Olivia', 'History', 3),
        ('King', 'Lucas', 'Geography', 1)
    ]
    query = """
        INSERT INTO students(last_name, first_name, specialization, school_id)
        VALUES (?, ?, ?, ?)
    """
    cursor.executemany(query, students)

    query = """
        SELECT students.id, students.last_name, students.first_name, students.specialization, schools.school_number, schools.address 
        FROM students
        LEFT JOIN schools ON students.school_id = schools.id
    """
    result = cursor.execute(query)
    pprint(result.fetchall(), width=100)

    query = """
        ALTER TABLE students
        ADD COLUMN phone_number TEXT
    """
    cursor.execute(query)

    query = """
        UPDATE students
        SET phone_number = '38099659418'
        WHERE id = 5
    """
    cursor.execute(query)

    query = """
        DELETE FROM students
        WHERE id BETWEEN 2 AND 4
    """
    cursor.execute(query)

    query = """
        SELECT * FROM students
        ORDER BY id DESC
        LIMIT 3 OFFSET 2
    """
    result = cursor.execute(query)
    pprint(result.fetchall(), width=100)
