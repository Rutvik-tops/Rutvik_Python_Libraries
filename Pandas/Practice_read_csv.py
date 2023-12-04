#!/usr/bin/env python
# coding: utf-8

# 
# # Practice

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


R=pd.read_csv("data.csv")
R


# In[3]:


R.head(100)


# In[4]:


R.columns


# In[5]:


k=R.dtypes
k


# In[6]:


k=R.isnull()
k

print()
k=R.isnull().sum()


# In[7]:


m=1000
R[R.isnull()] = m
print(R)


# In[8]:


R["Rutvik"]= R["Calories"] <= 1000
R


# In[9]:


S=R.pop("Rutvik")
S


# In[10]:


R.columns


# In[11]:


R


# In[18]:


R.sample(50)


# In[19]:


R.columns


# In[27]:


R["Duration"].where(R["Duration"]>60,1000)


# In[23]:


R.isnull().sum()


# In[32]:


R["Duration"].unique()


# In[35]:


Duration=[60,45,80]
R[R.Duration.isin(Duration)]


# In[38]:


R.replace(0,20000)


# In[45]:


Z=R.rename(columns={"Duration" :"Rutvik"})


# In[43]:


R.head()


# In[46]:


Z


# In[ ]:




