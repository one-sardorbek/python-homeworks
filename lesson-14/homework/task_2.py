import numpy as np
array_1=np.array([2, 3, 4, 5]) 
array_2=np.array([1, 2, 3, 4])
@np.vectorize
def pow(a,b):
    return a**b
pow_array=pow(array_1,array_2)
print(pow_array)
    