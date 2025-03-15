import numpy as np

# Create a 3x3 matrix with random values
A = np.random.rand(3, 3)

# Compute the determinant
determinant = np.linalg.det(A)

print("Matrix A:\n", A)
print("\nDeterminant of A:", determinant)
