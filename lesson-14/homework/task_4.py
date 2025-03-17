import numpy as np
W=np.array([[10,-2,3],[-2,8,-1],[3,-1,6]])
Y=np.array([12,-5,15])
solution=np.linalg.solve(W, Y)
print("I1=",solution[0],"\nI2=",solution[1],"\nI3=",solution[2])
