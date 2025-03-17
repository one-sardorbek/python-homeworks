import numpy as np
W=np.array([[4,5,6],[3,-1,1],[2,1,-2]])
Y=np.array([7,4,5])
solution=np.linalg.solve(W, Y)
print(solution)
