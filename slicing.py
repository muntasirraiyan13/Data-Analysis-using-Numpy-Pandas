# 1D slicing (start:stop:step)
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(arr[1:4])
print(arr[1:4:2])

#2D slicing (row_start : row_end : step, col_start : col_end:step)
arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2)
print(arr2[1:3, 1:3])
print(arr2[::2, ::2])
