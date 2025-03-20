import numpy as np
import matplotlib.pyplot as plt

# Define x values for each function
x1 = np.linspace(-2, 2, 100)
x2 = np.linspace(-2 * np.pi, 2 * np.pi, 100)
x3 = np.linspace(-2, 2, 100)
x4 = np.linspace(0, 2, 100)

# Compute function values
y1 = x1**3
y2 = np.sin(x2)
y3 = np.exp(x3)
y4 = np.log(x4 + 1)

# Create figure and subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Top-left: x^3
axes[0, 0].plot(x1, y1, 'r')
axes[0, 0].set_title("$f(x) = x^3$")
axes[0, 0].set_xlabel("x")
axes[0, 0].set_ylabel("f(x)")

# Top-right: sin(x)
axes[0, 1].plot(x2, y2, 'g')
axes[0, 1].set_title("$f(x) = \sin(x)$")
axes[0, 1].set_xlabel("x")
axes[0, 1].set_ylabel("f(x)")

# Bottom-left: e^x
axes[1, 0].plot(x3, y3, 'b')
axes[1, 0].set_title("$f(x) = e^x$")
axes[1, 0].set_xlabel("x")
axes[1, 0].set_ylabel("f(x)")

# Bottom-right: log(x+1)
axes[1, 1].plot(x4, y4, 'm')
axes[1, 1].set_title("$f(x) = \log(x+1)$")
axes[1, 1].set_xlabel("x")
axes[1, 1].set_ylabel("f(x)")

# Adjust layout for better spacing
plt.tight_layout()

# Show plot
plt.show()
