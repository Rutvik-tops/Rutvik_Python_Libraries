#!/usr/bin/env python
# coding: utf-8

# # Create array

# In[1]:


import numpy as np


# In[19]:


R=np.array([1,2,3,4,5] ,ndmin=5)
R

print(R)
print()
print("Array Value type",R.dtype)
print()
print("type of Dimention:",type(R))
print()
print("Type of Array : ",R.ndim)


# In[23]:


R=np.array([1,2,3,4,5])

print("Indexing : ",R[1])


# In[25]:


R=np.array([1,2,3,4,5])
print("addition of array : ",R[1]+R[2])


# # 3D Indexing

# In[29]:


import numpy as np

s=np.array([[[1,23,43],[1,45,64]],[[2,65,88],[1,56,76]]])
print(s)
print()
print("Number of Dimention : ",s.ndim)
print()
print("Type of Dimention : ",type(s))
print()
print("type of value : ",s.dtype)
print()
print("Indexing in 3D array : ",s[0,1,1])
print()
print("Reshape Array : ")
print(s.reshape(12,1))
print()
print("Array Slicing : ")
print()
print(s[1:3])

