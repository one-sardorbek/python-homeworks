import numpy as np

# Generate a 5x5 matrix with random values
matrix = np.random.randint(0,100,(5, 5))  # Random values between 0 and 1

# Normalize the matrix
matrix_min = matrix.min()
matrix_max = matrix.max()
normalized_matrix = (matrix - matrix_min) / (matrix_max - matrix_min)

print("Original Matrix:\n", matrix)
print("\nNormalized Matrix:\n", normalized_matrix)