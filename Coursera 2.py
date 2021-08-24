


                                  Coursera:2
                                  
# 1d numpy:

import numpy as np

a = np.array([0, 1, 2, 3, 4])    
    
type(a)    
    
a.dtype
a.shape  
a.ndim
a.size

b = np.array([0, 1.2, 2.5, 3, 4]) 

b.dtype

# indexing and slicing:
    
b[1] = 50
b[1] 

# vector

u = np.array([1,0])
v = np.array([0,1])
z = []

for n,m in zip(u,v):
    z.append(n+m)
  
print(z)

# or using numpy:
    
u = np.array([1,0])
v = np.array([0,1])
z = u+v
print(z)

# scaling:
# 1. using numpy:
y = np.array([1,2])
z = 2*y
print(z)

# using convenional method:

y = [1,2]
z = []
for n in y:
    z.append(2*n)
    
print(z)

# product:

# conventional    
u = [1,2]
v = [3,2]
z = []

for n,m in zip(u,v):
    z.append(n*m)
    
print(z)

# numpy

u = np.array([1,2])
v = np.array([3,2])
z = u*v
print(z)

# Dot product:
    
u = np.array([1,2])
v = np.array([3,2])
z = np.dot(u,v)
print(z)

#mean

u = np.array([1,2,3])

u_mean = u.mean()
print(u_mean)

u_max = u.max()
print(u_max)

np.pi

x = np.array([0, np.pi/2, np.pi])
y = np.sin(x)
print(y)

np.linspace(2,8,num=5) 

# Plotting:
x  = np.linspace(0,2*np.pi, 100)
y = np.sin(x)

import matplotlib.pyplot as plt

%matplotlib inline
plt.plot(x,y)



# 2d numpy:
    
a = [11, 12, 13], [21, 22, 23], [31, 32, 33]]

A = np.array(a)
print(A)

A.ndim

#dot product:
    
A = np.array([[0, 1, 1], [1, 0, 1]])
A
B = np.array([[1, 1], [1, 1], [-1, 1]])
B
Z = np.dot(A,B)                                   # WHY!!!
z


a=np.array([0,1])
b=np.array([1,0])
np.dot(a,b) 

X=np.array([[1,0,1],[2,2,2]]) 
out=X[0,1:3]
out


X=np.array([[1,0],[0,1]])
Y=np.array([[2,2],[2,2]])
Z=np.dot(X,Y)
z


import pandas as pd
file = 'fileexample.csv'
df = pd.read_csv(file)














































