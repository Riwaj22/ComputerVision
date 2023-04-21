#!/usr/bin/env python
# coding: utf-8

# In[25]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[35]:


def imshow(title="image",image = None, size=10):
    w, h = image.shape[0],image.shape[1]
    asperct_ratio = w/h
    plt.figure(figsize=(size*asperct_ratio,size))
    plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()


# In[36]:


image = cv2.imread(r"C:\Users\97798\Desktop\land.jpg")
type(image)


# In[37]:


image_scaled = cv2.resize(image,None,fx=0.75,fy=0.75,interpolation= cv2.INTER_LINEAR )
imshow("linear interpolation",image_scaled)


# In[39]:


image_scaled = cv2.resize(image,None,fx=2,fy=2,interpolation= cv2.INTER_CUBIC )
imshow("cubic interpolation",image_scaled)


# In[41]:


image_scaled = cv2.resize(image,None,fx=2,fy=2,interpolation= cv2.INTER_NEAREST )
imshow("inter nearest",image_scaled)


# In[43]:


image_scaled = cv2.resize(image,(900,900),interpolation= cv2.INTER_AREA )
imshow("inter area",image_scaled)


# In[46]:


# Image Pyramids
image = cv2.imread(r"C:\Users\97798\Desktop\land.jpg")

smaller = cv2.pyrDown(image)
larger = cv2.pyrUp(smaller)

imshow("Original",image)
imshow("Smaller",smaller)
imshow("Larger",larger)

even_smaller = cv2.pyrDown(smaller)
imshow("Even smaller",even_smaller)


# In[50]:



image = cv2.imread(r"C:\Users\97798\Desktop\land.jpg")

height , width = image.shape[0],image.shape[1]

start_row, start_column = int(height*.25), int(width*.25)

end_row,end_column = int(height*0.75),int(width*0.75)

cropped =  image[start_row:end_row,start_column:end_column]
imshow("image",image)

copy = image.copy()
cv2.rectangle(copy,(start_column,start_row),(end_column,end_row),(0,255,255),2)
imshow("Area being cropped",copy)
imshow("Crpped Image",cropped)


# In[ ]:




