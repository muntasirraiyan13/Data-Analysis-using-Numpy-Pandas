# 1D sorting
import numpy as np
x=np.array([10,8,16,100])
z=x.copy()
print(z)
z.sort()
print(z)

sorted_array=np.sort(x)
print(sorted_array)
print(x)

#2D sorting
arr=np.array([[10,9,15],[20,8,12]])
print(arr.ndim)
print(arr.shape)
print(arr)
#horizontal sorting
sort_array=np.sort(arr,axis=1)
print(sort_array)
#vertical sorting
sort_array1=np.sort(arr,axis=0)
print(sort_array1)
