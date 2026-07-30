import numpy as np
arr=np.random.randint(1,10,(10,5))
b=arr.reshape(5,10)
print(b)

# Converting 2D array to 1D array
arr1=np.random.randint(1,100,(3,4))
print(arr1)
print(arr1.ndim)
c=arr1.flatten()
print(c)
print(c.ndim)
