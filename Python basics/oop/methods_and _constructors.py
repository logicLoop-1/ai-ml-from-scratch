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

#usage of __eq__
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __eq__(self, other):
        return (
            self.title == other.title
            and self.author == other.author
            and self.pages == other.pages
        )


book1 = Book("Happy Place", "Emily Henry", 334)
book2 = Book("Happy Place", "Emily Henry", 334)

print(book1 == book2)