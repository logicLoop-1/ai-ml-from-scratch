# Classes and Objects in Python


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self):
        return f"{self.title} is written by {self.author} and has {self.pages} pages."


# Creating objects
book1 = Book("Happy Place", "Emily Henry", 334)
book2 = Book("The Silent Patient", "Alex Michaelides", 336)

print(book1.title)
print(book2.title)

print(book1.summary())
print(book2.summary())