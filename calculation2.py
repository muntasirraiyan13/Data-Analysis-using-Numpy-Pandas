import numpy as np
arr=np.array([[1,2,9,9,10],[2,8,10,9,1]])
print(arr)
x=np.count_nonzero(arr==9)
y=np.count_nonzero(arr)
z=np.count_nonzero(arr<10)
p=np.unique(arr)


print(x)
print(y)
print(z)
print(p)
