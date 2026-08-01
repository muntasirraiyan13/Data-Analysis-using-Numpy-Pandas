import numpy as np
x=np.array([10,8,16,100])
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
index=np.where(x)
index1=np.where(x==8)
index2=np.where(arr==5)
index3=np.where(arr>4)
arr1=np.where(arr>4,arr,0)
print(index)
print(index1)
print(index2)
print(index3)
print(arr1)


