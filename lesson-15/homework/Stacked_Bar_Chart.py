import matplotlib.pyplot as plt
import numpy as np
categories=('Category A', 'Category B', 'Category C')
time_periods=('T1', 'T2', 'T3', 'T4')

data_A=[1,2,3,5]
data_B=[2,3,4,1]
data_C=[1,4,2,6]
fig,ax=plt.subplots()
x=np.arange(len(time_periods))
ax.bar(x,data_A, label="Category A", color="b")
ax.bar(x,data_B, bottom=data_A, label="Category B",color="r")
ax.bar(x,data_C, bottom=np.array(data_A)+np.array(data_B), label="Category C",color="g")

ax.set_title("Stacked bar chart")
ax.set_xlabel("Time periods")
ax.set_ylabel("Values")
ax.set_xticks(x)
ax.set_xticklabels(time_periods)
ax.legend()

plt.show()