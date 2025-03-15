import numpy as np

# Create a 3x3 matrix (A)
A = np.random.rand(3, 3)

# Create a 3x1 column vector (b)
b = np.random.rand(3, 1)

# Solve for x (Ax = b)
x = np.linalg.solve(A, b)

print("Matrix A (3x3):\n", A)
print("\nColumn Vector b (3x1):\n", b)
print("\nSolution x (3x1):\n", x)
