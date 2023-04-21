#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install opencv


# In[18]:


import cv2


# In[ ]:





# In[35]:


# load color image
image = cv2.imread(r'C:\Users\97798\Desktop\land.jpg')


# In[36]:


from matplotlib import pyplot as plt


# In[40]:


# our own function for showing the image
def imshow(title = "image",image = None, size=10):
    w,h = image.shape[0],image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize = (size *aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()


# In[41]:


# split to B,G,R seperately
B,G,R = cv2.split(image)
imshow('blue',B)
imshow('green',G)
imshow('red',R)


# In[ ]:


# Displaying Image Dimension


# In[42]:


import numpy as np


# In[54]:


print(image.shape)
print(B.shape)
print(G.shape)
print(R.shape)


# In[55]:


print("Height of image {} pixels".format(image.shape[0]))
print('Width of image {} pixels'.format(image.shape[1]))
print("Depth of image {} pixels".format(image.shape[2]))


# In[70]:



import numpy as np
zeros = np.zeros(image.shape[:2], dtype="uint8")
imshow('RED',cv2.merge([zeros,zeros,R]))
imshow('GREEN',cv2.merge([zeros,G,zeros]))
imshow('BLUE',cv2.merge([B,zeros,zeros]))


# In[72]:


B,G,R = cv2.split(image)

image = cv2.merge([B,G,R])
imshow('Merged',image)


# In[74]:


# lets modify blue color
merge = cv2.merge([B+100,G,R])
imshow('Blue Boost',merge)


# In[77]:


# # hsv color space
# convert to hsv

hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
imshow("hsv_image",hsv_image)


# In[81]:


# obtaining the h,s,v values

imshow('Hue',hsv_image[:,:,0])
imshow('Saturation',hsv_image[:,:,1])
imshow('Value',hsv_image[:,:,2])


# In[ ]:




