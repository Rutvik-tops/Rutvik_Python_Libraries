#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


X=np.array([2,23,56])
Y=np.array([5,56,78])


# In[3]:


X


# In[4]:


Y


# In[5]:


plt.plot(X,Y)
plt.show()


# In[6]:


plt.plot(X,Y,'o')
plt.show()


# In[7]:


plt.plot(X,marker='*')
plt.show()


# In[8]:


plt.plot(X,'o:r')
plt.show()


# In[9]:


plt.plot(X,'o:b',ms=15,mec="black")
plt.show()


# In[10]:


plt.plot(X,'o:b',ms=15,mec="black",mfc="r")
plt.show()


# In[11]:


plt.plot(X,Y,'o:b',ms=15,mec="black",linestyle="dashed")
plt.show()


# In[12]:


plt.plot(X,'o:b',ms=15,mec="black",linewidth="4.5")
plt.show()


# In[13]:


plt.plot(X)
plt.plot(Y)

plt.show()


# In[14]:


plt.plot(X , Y)

plt.xlabel("Marks")
plt.ylabel("RollNo")
plt.title("Demo Data",loc="left")

plt.show()


# In[15]:


plt.plot(X , Y)

plt.xlabel("Marks")
plt.ylabel("RollNo")
plt.title("Demo Data",loc="left")

plt.grid()
plt.show()


