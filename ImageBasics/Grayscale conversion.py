#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install opencv


# In[2]:


import cv2


# In[ ]:





# In[3]:


# load color image
image = cv2.imread(r"C:\Users\97798\Pictures\Screenshots\Screenshot 2023-03-21 101247.png")


# In[4]:


from matplotlib import pyplot as plt


# In[7]:


# our own function for showing the image
def imshow(title = "image",image = None, size=10):
    w,h = image.shape[0],image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize = (size *aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title("title")
    plt.show()


# In[8]:


imshow('Image',image)


# In[ ]:


# Displaying Image Dimension


# In[9]:


import numpy as np


# In[10]:


print(image.shape)


# In[11]:


print("Height of image {} pixels".format(image.shape[0]))
print('Width of image {} pixels'.format(image.shape[1]))
print("Depth of image {} pixels".format(image.shape[2]))


# In[13]:


# Grayscaling the image
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


# In[ ]:


# grayscale image has 1 dimension that is intensity of gray color
# O means black,absence of light
# 255 means pure white


# In[17]:


imshow("grayimage",image)
type(image)

