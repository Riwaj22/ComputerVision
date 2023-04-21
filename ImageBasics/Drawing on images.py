#!/usr/bin/env python
# coding: utf-8

# In[87]:



import cv2
import numpy as np
from matplotlib import pyplot as plt


# In[88]:


# load color image
image = cv2.imread(r'C:\Users\97798\Desktop\land.jpg')


# In[89]:


# our own function for showing the image
def imshow(title = "image",image = None, size=10):
    w,h = image.shape[0],image.shape[1]
    aspect_ratio = w/h
    plt.figure(figsize = (size *aspect_ratio,size))
    plt.imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.show()


# In[93]:


# create a block image using numpy to create and array of black
image = np.zeros([512,512,3], np.uint8)

# convert it to grayscale
gray_image = np.zeros([512,512],np.uint8)


imshow('RGB',image)
imshow('GRAY',gray_image)


# In[99]:


# draw a line
cv2.line(image,(0,0),(512,512),(225,127,0),1)
cv2.line(image,(100,100),(512,512),(225,166,0),4)
imshow("Black canvas with diagonal line",image)


# In[101]:


# draw rectangles
image1 = np.zeros([512,512,3],np.uint8)

cv2.rectangle(image1,(200,200),(300,250),(127,50,127),10)
imshow('Rectangle',image1)


# In[103]:


# draw circles
image = np.zeros([512,512,3],np.uint8)
cv2.circle(image,(350,350),100,(255,11,255),-1)
imshow('circle',image)


# In[104]:


# draw polygon
image = np.zeros([512,512,3],np.uint8)

# lets define points
pts = np.array([[10,50],[400,50],[50,200],[50,500]],np.int32)

# reshape our points in form required by polylines
pts= pts.reshape((-1,1,2))

cv2.polylines(image,[pts],True,(0,0,255),3)
imshow("polylines",image)


# In[109]:


# ADD TEXT

image = np.zeros([1000,1000,3],np.uint8) 
string = "Hello world"
cv2.putText(image,string,[100,100],cv2.FONT_HERSHEY_COMPLEX,4,(40,40,255),4)
imshow('Image',image)


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




