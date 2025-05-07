class Student:
    def __init__(self, name, student_id):
        "Initialized a Student with name, ID and an empty list for courses."
        self.name = name
        self.student_id = student_id
        self.courses = []


student1 = Student("Alice Smith", "S1001")
print(f"Student Name: {student1.name}")
print(f"Student ID: {student1.student_id}")
print(f"Courses: {student1.courses}")

