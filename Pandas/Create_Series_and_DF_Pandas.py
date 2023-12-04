#!/usr/bin/env python
# coding: utf-8

# # Create Series in Pandas
# 

# In[1]:


import pandas as pd


# In[2]:


d = pd.Series([1,2,3,5])
print(d)


# In[10]:


d = pd.Series([1,2,3,5])
print(d.to_string(index=False))
print()
print("Type Check : ",type(d))
print()
print("Indexing : ", d[0])


# In[30]:


k=pd.Series([1,3,5,7,9], index = ["A","B","C","D","E"])
print("Give Different Indexing \n ",k)
print()
print("Output on Indexing ",k["E"])


# In[31]:


d = pd.Series({"Name":"Rutvik","Std":10 })
print(d)


# 
# 
# # DataFrame

# In[46]:


p=pd.DataFrame({"Name":["Rutvik","Arpit"],"Std":[10,12]})
print(p)
print()
print("Location : ",p.loc[0])
print()
print("Location With two indexing : \n  ",p.loc[[0,1]])


# In[60]:


# Read CSV file

df=pd.read_csv('data.CSV')
#rint(df)
#nt(df.to_string())
print(df.to_csv('Rutvik_example',index=False))

