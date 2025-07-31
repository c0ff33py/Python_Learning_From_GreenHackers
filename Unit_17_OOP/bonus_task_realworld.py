# Task: Student Class Management System
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def promote(self):
        self.grade += 1

    def display(self):
        print(f"{self.name} is in Grade {self.grade}.")


# Create 3 students
s1 = Student("Alice", 9)
s2 = Student("Bob", 10)
s3 = Student("Mike", 5)

s1.promote()
s1.display()
s3.promote()
s2.display()
s3.display()
