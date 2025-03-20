import matplotlib.pyplot as plt
import numpy as np

mean=0
std=1
num_samples=1000
data=np.random.normal(mean,std,num_samples)

fig, ax=plt.subplots(figsize=(8,6))
ax.hist(data,bins=30,alpha=0.7,color="b",edgecolor="black")
ax.set_title("Histogram of Normally Distributed Data")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
ax.grid(True)

plt.show()