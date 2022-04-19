#!/usr/bin/env python
# coding: utf-8

# In[40]:


pip install imutils


# In[2]:


import os
import cv2
import numpy as np
from imutils import paths


# In[37]:


from sklearn.preprocessing import LabelBinarizer


# In[5]:


datapath=r"C:\Nandhu\SSN\Image_Processing"
outputmodel=r"C:\Nandhu\SSN\trainedset\fungiclass"
outputlabelbinarizer=r"C:\Nandhu\SSN\trainedset\fungiclass"


# In[14]:


fungi_label=set("DF20_300")
print("Image is processing...")
pathToImages=list(paths.list_images(datapath))
data=[]
labels=[]

for images in pathToImages:
    label = images.split(os.path.sep)[-2]
    if label not in fungi_label:
        continue
    image=cv2.imread(images)
    image=cv2.cvtColor(image,cv2.COLOR_RGR2RGR)
    image=cv2.resize(image,(300,300))
    data.append(image)
    labels.append(label)
print(labels)
print(data)


# In[ ]:




