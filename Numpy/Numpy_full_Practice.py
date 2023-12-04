#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[49]:


p=np.array([[1,2,4,5,6],[2,5,7,8,9]],ndmin=5)
p
print()
print("Type of Dimention : ",type(p))


# In[28]:


print("Number of Dimention : ",p.ndim)


# In[16]:


r=np.array((1,4,5,6,7))
r


# In[18]:


r[0]
print()
r


# In[41]:


r=np.array((1,4,5,6,7),ndmin=5)
r
print(r.ndim)
#print("Indexing in Numpy : ",r[0,2])


# In[31]:


print("Slicing in numpy : ",r[0,1:3])


# In[34]:


print("Data Type : ",r.dtype)


# In[43]:


print("Type of Shape : ",r.shape)


# In[46]:


print("Reshape : ",r.reshape(5,1))


# In[50]:


# itaration
k=np.array([1,5,78,9,4])
k
for i in k:
    print(i)


# In[55]:


s=np.array([[1,2,4,5,6],[2,5,7,8,9]],ndmin=5)
s
for r in np.nditer(s):
    print(r,end=" ")
    


# In[60]:


#join method in numpy
m=np.array((1,2,4,5,7))
k=np.array((3,5,7,8,9))
j=np.concatenate((k,m))
j


# In[62]:


#Search Method in numpy
x=np.where(m==4)
x


# In[64]:


#SearchSorted method in numpy

z=np.searchsorted(k,3)
z


# In[65]:


#Sort method in numpy
print(np.sort(j))

