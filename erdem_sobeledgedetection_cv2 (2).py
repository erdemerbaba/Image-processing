#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:38:08 2020

@author: internet
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('baloon.jpg',0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=15)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=15)
sob = np.hypot(sobelx, sobely)

plt.subplot(3,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(3,3,5),plt.imshow(sob,cmap = 'gray')
plt.title('Sobel filter'), plt.xticks([]), plt.yticks([])
