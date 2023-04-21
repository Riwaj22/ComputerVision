#!/usr/bin/env python
# coding: utf-8

# In[134]:



import cv2
import numpy as np
from matplotlib import pyplot as plt


# In[135]:


# load color image
image = cv2.imread(r'C:\Users\97798\Desktop\land.jpg')


# In[136]:


# our own function for showing the image
def imshow(title = "image",image = None, size=10):
    w,h = image.shape[0],image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize = (size *aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()


# In[137]:


imshow("image",image)


# In[139]:


# Translations

image = cv2.imread(r'C:\Users\97798\Desktop\land.jpg')

imshow('original',image)
height,width = image.shape[:2]

# we shift height and weight 
quarter_height , quarter_width = height/4,width/4

T = np.float32([[1,0,quarter_width],[0,1,quarter_height]])
image_translations = cv2.warpAffine(image,T,(width,height))
imshow("Translations",image_translations)


# In[141]:


print(T)
print(height,width)


# In[145]:


# Rotations
image = cv2.imread(r'C:\Users\97798\Desktop\land.jpg')

imshow('original image',image)
height,width = image.shape[:2]

rotation_matrix = cv2.getRotationMatrix2D((width/3,height/5),45,1)
rotated_image = cv2.warpAffine(image,rotation_matrix,(width,height))
imshow("Rotated image",rotated_image)


# In[149]:


# Scaling image
rotation_matrix = cv2.getRotationMatrix2D((width/3,height/2),135,0.5)
rotated_image = cv2.warpAffine(image,rotation_matrix,(width,height))
imshow("Rotated image",rotated_image)


# In[151]:


# Transpose
imshow('original image',image)
rotated_image = cv2.transpose(image)
imshow("Rotated using Transform",rotated_image)


# In[159]:


# ADD TEXT

string = "Hello world"
cv2.putText(image,string,[1,1],cv2.FONT_HERSHEY_COMPLEX,4,(1,1,255),3)
imshow('Image',image)


# In[158]:


# flip image
image = cv2.imread(r'C:\Users\97798\Desktop\land.jpg')
flipped = cv2.flip(image,1)
imshow("flipped image",flipped)


# In[ ]:




