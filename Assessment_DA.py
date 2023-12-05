#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q.1 Convert a 1D array to a 2D array with 2 rows

import numpy as np

A=np.array([1,2,3,4,5])
A
print("Before Number of Dimention : ",A.ndim)
print("")
A=np.array([1,2,3,4,5],ndmin=2)
A
print("After Number of Dimention : ",A.ndim)


# In[2]:


#Q.2 Get the common items between a and b

a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])

Common_number=np.intersect1d(a,b)
print(Common_number)


# In[3]:


#Q.3 Get all items between 5 and 10 from a. 
 
a = np.array([2, 6, 1, 9, 10, 3, 27])

Result=a[(a>=5)&(a<=10)]
print(Result)



# In[4]:


#Q.4 Limit the number of items printed in python NumPy array a to a maximum of 6 elements. 

a=np.array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

np.set_printoptions(threshold=6 , edgeitems= 3)
a


# In[5]:


import pandas as pd 


# In[6]:


# 1. Compute the minimum, 25th percentile, median, 75th, and maximum of ser.

 
ser = pd.Series([1, 2, 3, 4, 5])

# Using describe() to get summary statistics
summary_stats = ser.describe(percentiles=[.25, .5, .75])

# Extracting specific percentiles from the summary
minimum = summary_stats['min']
percentile_25 = summary_stats['25%']
median = summary_stats['50%'] 
percentile_75 = summary_stats['75%']
maximum = summary_stats['max']

# Display the results
print("Minimum:", minimum)
print("25th Percentile:", percentile_25)
print("Median:", median)
print("75th Percentile:", percentile_75)
print("Maximum:", maximum)


# In[7]:


#2. Creating A Pandas Data Frame and Using Sample Data Sets


# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'Math_Score': [90, 85, 78, 92, 88],
    'English_Score': [85, 88, 90, 80, 92],
    'Science_Score': [88, 92, 85, 78, 90]
}


df = pd.DataFrame(data)


print(df)


# In[8]:


# 3. Using NumPy, create a Pandas Data Frame with five rows and three columns.

data = np.random.rand(5, 3)

# Create a Pandas DataFrame with the NumPy array
df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3'])

print(df)


# In[10]:


"""4. For a Pandas Data Frame created from a NumPy array, what is the default behavior for 
the labels for the columns? For the rows?"""

import pandas as pd
import numpy as np


data = np.array([[1, 2, 3], [4, 5, 6]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'], index=['row1', 'row2'])

df



# In[16]:


"""5. take csv file contains at least 10,000 rows and 12 columns which numerical and text values 
according to that continue following steps."""

R = pd.read_csv('C:\\Users\\Lenovo\\Downloads\\10000_demo.csv')


# In[22]:


#6. Write the code to show the number of rows and columns in data frame

S=pd.DataFrame(R)
S
print()
K=S.shape
K


# In[26]:


#7. How might you show the first few rows of data frame?


M=S.head()
M


# In[33]:


#9. Create a line plot using the x and y values provided below. Label the y-axis as “Y” and label the x-axis as “X”. 

import matplotlib.pyplot as plt 

x = [3, 4, 5, 6] 
y = [1.5, 2, 2.5, 3]

plt.plot(x,y)

plt.xlabel('x')
plt.xlabel('y')

plt.show()



# In[34]:


"""10. Create an array of numbers between 0 and 6 with increments of 0.3 and name its “x”. 
Then on the same plot, plot x, x², x³, and x⁴. For consistency, use the following style lines 
respectively, “ro”, “bs”, “g”, and “:”. Lastly, make sure that the x-axis covers 0 to 6, while 
the y-axis spans from 0 to 125. Do not worry if you are not familiar with the style lines — 
you will recognize them as soon as you see the plot."""


# Create an array 'x' with increments of 0.3
x = np.arange(0, 6.3, 0.3)

# Plot x, x², x³, and x⁴ with specified style lines
plt.plot(x, x, 'ro', label='x')
plt.plot(x, x**2, 'bs', label='x²')
plt.plot(x, x**3, 'g', label='x³')
plt.plot(x, x**4, ':', label='x⁴')

# Set x-axis and y-axis limits
plt.xlim(0, 6)
plt.ylim(0, 125)

# Add labels to the axes
plt.xlabel('X')
plt.ylabel('Y')

# Add a legend
plt.legend()

# Display the plot
plt.show()


# In[35]:


""" 11. Heights and initials of a group of individuals are provided below. Create a bar plot titled 
“Height Comparison” to compare the heights among this group. 
height = [179, 155, 191, 152, 188, 177] 
names = ['QA', 'WB', 'EC', 'RD', 'TE', 'YF']"""


# Heights and names
height = [179, 155, 191, 152, 188, 177]
names = ['QA', 'WB', 'EC', 'RD', 'TE', 'YF']

# Create a bar plot
plt.bar(names, height, color='blue')

# Add title and labels to the axes
plt.title('Height Comparison')
plt.xlabel('Names')
plt.ylabel('Height (cm)')

# Display the plot
plt.show()


# In[36]:


"""12. Plot a histogram of x, where x consists of 100,000 randomly-selected points with a normal 
distribution (hint: you can use numpy.random.randn() to generate the random points). The 
histogram should have 10 bins. Look at how the histogram changes when we try 20 and 50 
bins."""

import numpy as np
import matplotlib.pyplot as plt

# Generate 100,000 random points with a normal distribution
x = np.random.randn(100000)

# Plot the histogram with 10 bins
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.hist(x, bins=10, color='blue', edgecolor='black')
plt.title('Histogram with 10 Bins')

# Plot the histogram with 20 bins
plt.subplot(1, 3, 2)
plt.hist(x, bins=20, color='green', edgecolor='black')
plt.title('Histogram with 20 Bins')

# Plot the histogram with 50 bins
plt.subplot(1, 3, 3)
plt.hist(x, bins=50, color='orange', edgecolor='black')
plt.title('Histogram with 50 Bins')

plt.tight_layout()
plt.show()


# In[37]:


#13. What are the features of TensorFlow?

"""1. **Flexibility and Compatibility:**
   - Supports diverse hardware platforms, including CPUs, GPUs, and TPUs.

2. **Comprehensive Ecosystem:**
   - Offers a rich set of tools, libraries, and community resources.

3. **Scalability:**
   - Scales seamlessly from individual devices to distributed computing systems.

4. **Deep Learning Support:**
   - Provides high-level APIs like Keras for building and training neural networks.

5. **TensorFlow Lite and TFX:**
   - Enables deployment on mobile devices (TensorFlow Lite) and offers end-to-end production-ready capabilities (TFX)."""


# In[38]:


#14. List a few limitations of TensorFlow.

"""Steep Learning Curve:

TensorFlow can have a challenging learning curve for beginners, especially when dealing with lower-level APIs.
Verbosity:

Writing TensorFlow code can be verbose, requiring more lines of code compared to some other frameworks.
Community Support for Older Versions:

Updates to newer versions may result in reduced community support for older TensorFlow versions.
Debugging Challenges:

Debugging TensorFlow code can be complex, and error messages may not always be straightforward.
Integration Overhead:

Integrating TensorFlow into existing workflows can sometimes require additional effort due to its comprehensive nature."""


# In[39]:


#15. What do you know about supervised and unsupervised machine learning?

"""**Supervised Learning:**
- **Objective:** Maps input data to labeled output.
- **Training Data:** Requires labeled examples.
- **Prediction:** Makes predictions on new, unseen data.

**Unsupervised Learning:**
- **Objective:** Finds patterns in unlabeled data.
- **Training Data:** Involves unlabeled examples.
- **Tasks:** Includes clustering and dimensionality reduction.

**Key Differences:**
- **Feedback:** Supervised gets explicit feedback; unsupervised explores data structure.
- **Tasks:** Supervised for classification/regression; unsupervised for clustering/pattern discovery.
"""


# In[ ]:




