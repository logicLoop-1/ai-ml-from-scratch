import numpy as np

# Q1: Create a NumPy array from [5, 10, 15, 20, 25]. Print its shape, size, and dtype.
arr = np.array([5, 10, 15, 20, 25])
print(arr.shape)
print(arr.size)
print(arr.dtype)

# Q2: Create a 3x3 matrix using np.arange and .reshape(), containing numbers 1 through 9.
arr1 = np.arange(1, 10)
reshaped = arr1.reshape(3, 3)
print(reshaped)

# Q3: Given arr, use boolean masking to get only the values greater than 30.
arr2 = np.array([12, 45, 7, 23, 56, 89, 34])
passing = arr2[arr2 > 30]
print(passing)

# Q4: Given a 2D array grades, calculate each student's average score, and the overall class average.
grades = np.array([[85, 90, 78], [92, 88, 95], [60, 70, 65]])
student_avg = grades.mean(axis=1)
print(student_avg)
overall_avg = grades.mean()
print(overall_avg)

# Q5: Compute dot product, and separately compute element-wise product.
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])
print(np.dot(a, b))
print(a * b)

# Q6: Extract just the middle column, then extract just the last row, using slicing.
matrix = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
print(matrix[:, 1])
print(matrix[2])

# Q7: Create a 1x3 vector and add it to a 3x3 matrix using broadcasting.
matrix1 = np.array([[6, 7, 8], [3, 9, 2], [1, 5, 4]])
vector = np.array([4, 7, 1])
print(matrix1 + vector)

# Q8: Convert temps_celsius to Fahrenheit in a single line.
temps_celsius = np.array([0, 20, 37, 100])
fahrenheit = (temps_celsius * 9 / 5) + 32
print(fahrenheit)