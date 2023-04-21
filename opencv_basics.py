#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install opencv


# In[3]:


import cv2


# In[4]:


print(cv2.version)


# In[5]:


image = cv2.imread(r"C:\Users\97798\Pictures\Screenshots\Screenshot 2023-03-21 101247.png")


# In[6]:


from matplotlib import pyplot as plt


# In[10]:


cv2.imshow("First image",image)
cv2.waitKey(0)


# In[11]:


cv2.imwrite('output.jpg',image)


# In[ ]:


# Displaying Image Dimension


# In[12]:


import numpy as np


# In[13]:


print(image.shape)


# In[15]:


print("Height of image {} pixels".format(image.shape[0]))
print('Width of image {} pixels'.format(image.shape[1]))
print("Depth of image {} pixels".format(image.shape[2]))


# In[ ]:




