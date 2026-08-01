import numpy as np
x=np.array([[10,30,20],[20,10,80]])
y=np.array([[20,30,10],[30,10,15]])
sum=x+y 
print(sum)
z=x.reshape(3,2)
p=y.reshape(6,1)
n=sum.reshape(6,1)
print(z)
print(p)
print(n)
