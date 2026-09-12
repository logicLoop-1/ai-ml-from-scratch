# Inheritance in Python


class Vehicle:
    def __init__(self, speed, brand):
        self.speed = speed
        self.brand = brand

    def describe(self):
        return "This is a vehicle."


class Car(Vehicle):
    def describe(self):
        return "This is a car."


class Motorcycle(Vehicle):
    def describe(self):
        return "This is a motorcycle."


vehicle1 = Vehicle(77, "Toyota")
car1 = Car(55, "Honda")
motorcycle1 = Motorcycle(77, "Yamaha")

print(vehicle1.describe())
print(car1.describe())
print(motorcycle1.describe())

print(car1.brand)
print(car1.speed)