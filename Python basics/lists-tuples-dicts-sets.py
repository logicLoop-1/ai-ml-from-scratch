# Lists, Tuples, Dictionaries and Sets in Python


# --------------------
# LISTS
# --------------------

movies = ["La La Land", "The Fault in Our Stars", "Cinderella", "Frozen"]

# Accessing elements
print(movies[1])
print(movies[-1])

# Adding an element
movies.append("The Hulk")

# Removing an element
movies.remove("La La Land")

print(movies)

# Changing an element
movies[0] = "Moana"
print(movies)

# Length of a list
print(len(movies))


# --------------------
# TUPLES
# --------------------

# Tuples are ordered and cannot be changed

coordinates = (10, 20)

print(coordinates)
print(coordinates[0])
print(coordinates[-1])

# Tuple unpacking
x, y = coordinates

print("x:", x)
print("y:", y)

# Swapping variables using tuple unpacking
a = 5
b = 10

a, b = b, a

print("a:", a)
print("b:", b)


# --------------------
# DICTIONARIES
# --------------------

student = {
    "name": "Menka",
    "age": 20,
    "gpa": 3.35
}

# Accessing values
print(student["name"])
print(student["gpa"])

# Adding a new key-value pair
student["major"] = "Computer Science"

# Updating a value
student["gpa"] = 3.44

print(student)

# Looping through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")


# --------------------
# SETS
# --------------------

# Sets do not store duplicate values

numbers = {1, 2, 2, 3, 3, 3, 4}

print(numbers)

# Adding an element
numbers.add(5)

print(numbers)

# Removing an element
numbers.remove(1)

print(numbers)

# Set operations

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union
print("Union:", set_a | set_b)

# Intersection
print("Intersection:", set_a & set_b)

# Difference
print("Difference:", set_a - set_b)