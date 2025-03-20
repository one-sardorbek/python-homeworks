import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,2/(np.pi))
sin=np.sin(x)
cos=np.cos(x)
plt.plot(sin,c="blue",marker="o",label=r"$f(x)=sinx$")
plt.plot(cos,c="red",marker=">",label=r"$f(x)=cos(x)$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
