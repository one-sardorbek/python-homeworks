import numpy as np

# Create a 5x3 matrix with random values
A = np.random.rand(5, 3)

# Create a 3x2 matrix with random values
B = np.random.rand(3, 2)

# Matrix multiplication (real matrix product)
result = np.dot(A, B)  # Alternatively: A @ B

print("Matrix A (5x3):\n", A)
print("\nMatrix B (3x2):\n", B)
print("\nResulting Matrix (5x2):\n", result)