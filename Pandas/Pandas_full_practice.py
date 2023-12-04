#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


R=pd.Series([1,3,6],index=["A","B","C"])
R
print(type(R))


# In[3]:


print(R[0])


# In[4]:


print(R)


# In[5]:


#New Data Fream

k={
    "Name":["Mahesh","Raj","Rutvik","Shubh"],
    "Age":[15,16,25,36]
}
m=pd.DataFrame(k)


# In[6]:


m.head()


# In[9]:


print(m.iloc[2])


# In[10]:


print(m.loc[1:3])


# In[ ]:




