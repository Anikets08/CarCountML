# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NA3FmVAz8aR2YLRjbud6NdUDdTqW-Yoh
"""

pip install cvlib

import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
im = cv2.imread('/content/1_0YyilCiA-lKLNNTZ1QO6rw.jpeg')
bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()
print('Number of cars in the image is '+ str(label.count('car')))

a = (label.count("car"))
b = a*2
print(b)

import time 
for i in range (b+1) :
  time.sleep(1)
  print(i)

from IPython.display import Image
print()
print("Red Signal")
print()

Image('/content/58afdad6829958a978a4a693.png',width= 100,height=100)