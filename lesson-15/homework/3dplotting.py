import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection ='3d')
x=np.linspace(-5,5,50)
y=np.linspace(-5,5,50)
X,Y=np.meshgrid(x,y)
Z= np.cos(X**2 + Y**2)
 
 
surf = ax.plot_surface(X, Y, Z, cmap="viridis")
fig.colorbar(surf)
ax.set_title("3D plotting")
ax.set_label(r"$f(x,y)=cos(x^2+y^2)$")
plt.show()