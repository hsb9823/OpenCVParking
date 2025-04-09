import cv2
import numpy as np

img = cv2.imread('image/zoomout.jpg', cv2.IMREAD_GRAYSCALE)
r, c = img.shape[:2]
print(r, c)

ratioX = 2
ratioY = 2

scaleimg = np.zeros((int(r * ratioY), int(c * ratioX)), np.uint8)
print(scaleimg.shape[0], scaleimg.shape[1])

for y in range(r):
    for x in range(c):
        i, j = int(y * ratioY), int(x * ratioX)
        scaleimg[i, j] = img[y, x]


cv2.imshow('original', img)
cv2.imshow('scale', scaleimg)
# cv2.imwrite('image/zoomout.jpg', scaleimg)

cv2.waitKey(0)
cv2.destroyAllWindows()