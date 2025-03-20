import matplotlib.pyplot as plt
import numpy as np

x=np.random.uniform(0,10,100)
y=np.random.uniform(0,10,100)

colors = np.random.rand(100)
markers = np.random.choice(['o', 's', 'D', '^', 'v'], size=100)

fig, ax = plt.subplots(figsize=(8, 6))
# Plot each point with a different marker
for i in range(100):
    ax.scatter(x[i], y[i], color=plt.cm.viridis(colors[i]), marker=markers[i])

# Customize plot
ax.set_title("Random Scatter Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.grid(True)

# Show plot
plt.show()
