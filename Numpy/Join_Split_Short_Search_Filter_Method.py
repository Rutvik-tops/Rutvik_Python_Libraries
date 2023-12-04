#!/usr/bin/env python
# coding: utf-8

# # Join Method
# 

# In[69]:


import numpy as np


# In[70]:


R=np.array([1,2,4,6,7])
R
print()
P=np.array([3,5,7,2,5])
P
print()
K=np.concatenate((R,P))
print(K)
print()
print("Number Of Dimention : ",K.ndim)


# In[71]:


R=np.array([[1,2,4,6,7],[3,4,6,8,8]])
R
print()
P=np.array([[3,5,7,2,5],[4,5,8,5,4]])
P
print()
K=np.concatenate((R,P),axis=1)
print(K)
print()
print("Number of Dimention : ",K.ndim)


# In[72]:


R=np.array([1,2,4,6,7])
R
print()
P=np.array([3,5,7,2,5])
P
print()
K=np.stack((R,P))
print(K)
print()
print("Number of Dimention : ",K.ndim)


# In[73]:


R=np.array([1,2,4,6,7])
R
print()
P=np.array([3,5,7,2,5])
P
print()
K=np.hstack((R,P))
print(K)
print()
print("Number of dimention : ",K.ndim)


# In[74]:


R=np.array([1,2,4,6,7])
R
print()
P=np.array([3,5,7,2,5])
P
print()
K=np.vstack((R,P))
print(K)
print()
print("Number of Dimention : ",K.ndim)


# In[75]:


R=np.array([1,2,4,6,7])
R
print()
P=np.array([3,5,7,2,5])
P
print()
K=np.dstack((R,P))
print(K)
print()
print("Number of Dimention : ",K.ndim)


# # Spliting Method

# In[76]:


R=np.array([1,2,4,6,7])
R
print()
K=np.array_split(R,3)
print(K)


# In[77]:


R=np.array([1,2,4,6,7])
R
print()
K=np.array_split(R,3)
print(K[0])
print(K[1])
print(K[2])


# In[78]:


R = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.hsplit(R, 3)

print(newarr)


# # Search

# In[79]:


R=np.array([1,2,4,6,7])
R
print()
P=np.searchsorted(R,7)
print(P)


# In[80]:


R=np.array([1,2,4,6,7])
R
print()
P=np.searchsorted(R,6,side='right')
print(P)


# In[81]:


R=np.array([1,2,4,6,7])
R
print()
P=np.searchsorted(R,[3,5,8])
print(P)


# # Short Method

# In[82]:


R=np.array([1,8,4,5,7])
R
P=print(np.sort(R))


# In[ ]:




