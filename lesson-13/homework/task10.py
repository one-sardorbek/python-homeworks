import numpy as np

# Create a 4x4 matrix with random values
A = np.random.rand(4, 4)

# Compute the transpose
A_transpose = np.transpose(A)  # Alternatively, A.T

print("Original Matrix:\n", A)
print("\nTranspose of the Matrix:\n", A_transpose)
