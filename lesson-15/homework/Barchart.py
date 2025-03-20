import matplotlib.pyplot as plt
import numpy as np
categories = ['Product A', 'Product B', 'Product C', 'Product D',"Product E"]
values = [200, 150, 250, 175, 225]

plt.bar(categories, values, color=("b","g","r","k","y","b"))
plt.title('Basic Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()