import numpy as np

# Vector addition
a = np.array([2, -1, 3])
b = np.array([4, 5, -2])
print(a + b)          # should match your answer: [6, 4, 1]

# Scalar multiplication
print(4 * np.array([1, -2, 3]))    # should match: [4, -8, 12]

# Magnitude
v = np.array([6, 8])
print(np.linalg.norm(v))            # should match: 10.0

# Dot product
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(np.dot(x, y))                  # should match: 32

# House price dot product
features = np.array([2000, 4, 2])
weights = np.array([150, 20000, -1000])
print(np.dot(features, weights))    # should match: 378000

# Matrix multiplication
A = np.array([[2, 0], [1, 3]])
B = np.array([[1, 3], [2, 1]])
print(A @ B)                         # should match: [[2, 6], [7, 6]]