# Loops and Functions in Python


# --------------------
# FOR LOOP
# --------------------

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)


# Print even numbers from 1 to 10

for num in range(1, 11):
    if num % 2 == 0:
        print(num)


# Print numbers divisible by 7 from 1 to 50

for num in range(1, 51):
    if num % 7 == 0:
        print(num)


# --------------------
# WHILE LOOP
# --------------------

# Number guessing game

target = 7
guess = None
attempts = 0

while guess != target:
    guess = int(input("Guess the number: "))
    attempts += 1

print(f"Good job! It took you {attempts} attempts.")


# --------------------
# BREAK AND CONTINUE
# --------------------

# Break

for num in range(1, 21):
    if num > 15:
        break

    print(num)


# Continue

for num in range(1, 11):
    if num % 3 == 0:
        continue

    print(num)


# --------------------
# NESTED LOOPS
# --------------------

# Triangle star pattern

for row in range(1, 6):
    for star in range(row):
        print("*", end="")
    print()


# --------------------
# FUNCTIONS
# --------------------

# Simple function

def greet():
    print("Hello, welcome to Python!")


greet()


# Function with parameter

def greet_user(name):
    print(f"Hello {name}!")


greet_user("Menka")


# Function with return value

def add(a, b):
    return a + b


result = add(5, 10)
print(result)


# Function to check if a number is even

def is_even(number):
    return number % 2 == 0


print(is_even(10))
print(is_even(7))


# --------------------
# FUNCTIONS WITH LOOPS
# --------------------

# Find the largest number

def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


numbers = [3, 7, 11, 2, 9, 4, 1, 12]

print("Largest number:", find_largest(numbers))


# --------------------
# STRING FUNCTION
# --------------------

# Check if a word is a palindrome

def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]


print(is_palindrome("madam"))
print(is_palindrome("hello"))


# --------------------
# DEFAULT ARGUMENT
# --------------------

def add_to_list(item, my_list=None):
    if my_list is None:
        my_list = []

    my_list.append(item)
    return my_list


print(add_to_list("a"))
print(add_to_list("b"))