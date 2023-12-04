#!/usr/bin/env python
# coding: utf-8

# # Sclicing & Iterating in Numpy

# In[1]:


import numpy as np


# In[34]:


R=np.array([1,2,4,6,7,8])
R
print()
print("Print Array : ",R)
print()
print("Number of Dimention : ",R.ndim)
print()
print("Sclicing : ",R[0:3])
print()
for i in R:
    print(i, end=" ")


# In[37]:


K=np.array([[1,2,3],[2,4,6]])
K
print()
print("Print Array : \n ",K)
print()
print("Number of Dimention : ",K.ndim)
print()
print("Sclicing : ",K[0,1:3])
print()
for i in np.nditer(P):
    print(i,end=" ")


# In[44]:


P=np.array([[[2,4,6,7],[3,4,6,8],[5,7,2,4]]])
P
print()
print("Print Array : \n ",P)
print()
print("Number of Dimention : ",P.ndim)
print()
print("Sclicing : ",P[0,2,2:])
print()
# for i in np.nditer(P,flags=['buffered'],op_dtypes=['S']):
    #print(i)
    
print()
for i in np.nditer(P[ : , : :2]):
    print(i)

