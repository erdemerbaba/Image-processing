#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:32:46 2020

@author: internet
"""
import numpy
data = numpy.zeros((240, 240, 3), dtype=numpy.uint8)

a=0
while a<240:
    data[a, 110] = [255, 0, 0]
    data[a, 120] = [0, 255, 0]
    data[a, 130] = [0, 0, 255]
    data[200,a]=[255,255,255]
    a=a+1
from PIL import Image
image = Image.fromarray(data)
image.show()