# Constructors and Methods


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Student: {self.name}"


student1 = Student("Menka")

student1.add_grade(55)
student1.add_grade(77)
student1.add_grade(88)

print(student1)
print("Average:", student1.average())