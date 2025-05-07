# day10/student_methods.py
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def add_course(self, course_name):
        """Adds a course to the student's list."""
        if course_name not in self.courses: # Avoid duplicates
            self.courses.append(course_name)
            print(f"Course '{course_name}' added for {self.name}.")
        else:
            print(f"{self.name} is already enrolled in '{course_name}'.")

    def list_courses(self):
        """Prints the list of courses for the student."""
        print(f"\nCourses for {self.name} ({self.student_id}):")
        if self.courses:
            for course in self.courses:
                print(f"  - {course}")
        else:
            print("  No courses enrolled yet.")

student1 = Student("Alice Smith", "S1001")
student1.list_courses()
student1.add_course("Math 101")
student1.add_course("Physics 201")
student1.add_course("Math 101") # Try adding duplicate
student1.list_courses()