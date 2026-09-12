# Polymorphism in Python


class Animal:
    def __init__(self, legs):
        self.legs = legs

    def speak(self):
        return "Normal animal sound."


class Cat(Animal):
    def speak(self):
        return "Meow meow"


class Dog(Animal):
    def speak(self):
        return "Bark bark"


class Goat(Animal):
    def speak(self):
        return "Mehh mehh"


cat = Cat(4)
dog = Dog(4)
goat = Goat(4)

animals = [cat, dog, goat]

for animal in animals:
    print(animal.speak())