#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 09:20:10 2020

@author: internet
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def tint(imag, percent):
    """
    imag: the image which will be shaded
    percent: a value between 0 (image will remain unchanged
             and 1 (image will completely white)
    """
    tinted_imag = imag + (np.ones(imag.shape) - imag) * percent
    return tinted_imag

windmills = plt.imread('underexposed.jpg')

tinted_windmills = tint(windmills, 0.3)
plt.axis("off")
plt.imshow(tinted_windmills)

cv2.imwrite("C:/Users/N/Desktop/my-image.png",tinted_windmills)

