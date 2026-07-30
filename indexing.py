import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])

arr1=np.array([1,2,3,4,5])
print(arr1)
for i in range(len(arr1)):
    print(arr1[i])

arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2)
for i in range(len(arr2)):
    for j in range(len(arr2[i])):
        print(arr2[i][j])

