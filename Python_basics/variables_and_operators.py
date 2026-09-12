# Variables and Operators in Python

# --------------------
# Variables
# --------------------

name = "Menka"
age = 20
gpa = 3.67
is_student = True

print(name)
print(age)
print(gpa)
print(is_student)


# --------------------
# Arithmetic Operators
# --------------------

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# --------------------
# Comparison Operators
# --------------------

x = 10
y = 5

print(x == y)   # Equal to
print(x != y)   # Not equal to
print(x > y)    # Greater than
print(x < y)    # Less than
print(x >= y)   # Greater than or equal to
print(x <= y)   # Less than or equal to


# --------------------
# Logical Operators
# --------------------

age = 20
has_id = True

print(age >= 18 and has_id)
print(age >= 18 or has_id)
print(not has_id)


# --------------------
# Assignment Operators
# --------------------

number = 10

number += 5
print(number)

number -= 3
print(number)

number *= 2
print(number)

number /= 4
print(number)


# --------------------
# String Concatenation
# --------------------

first_name = "Menka"
last_name = "Hotwani"

full_name = first_name + " " + last_name

print(full_name)

# Using f-string
print(f"My name is {first_name} {last_name} and I am {age} years old.")