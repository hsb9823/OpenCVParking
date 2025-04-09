import cv2
import numpy as np
# import matplotlib.pyplot as plt

img = cv2.imread('image/lena.png', cv2.IMREAD_COLOR)
cv2.imshow('lena original', img)

b, g, r = cv2.split(img)

colors = ['b', 'g', 'r']
cv2.imshow('img_b', b)


for color in colors:
    cv2.imshow('a', colors)

cv2.waitKey(0)
cv2.destroyAllWindows()

