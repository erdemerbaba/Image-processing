#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 14:13:46 2020

@author: internet
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt # import pylot

image_name="my-image2.png"
img=cv2.imread(image_name)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
size_y = img.shape[0] 
size_x=img.shape[1]
flattened=img.reshape([size_x*size_y])
rhist,_ ,_ = plt.hist(flattened, bins=256)# ,log=True)
plt.show() 
rhist,_ ,_ = plt.hist(flattened, bins=32)# ,log=True)
plt.show() # hist functions returns number values for each bin
rhist,_ ,_ = plt.hist(flattened, bins=8)# ,log=True)
plt.show() # hist functions returns number values for each bin