# 콜백 사용 X 컬러

import cv2
import numpy as np

def nothing(x):
    pass

image = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
while(1):
    cv2.imshow('image', image)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    image[:] = [b,g,r]

cv2.destroyAllWindows()
