# 콜백 사용 컬러 트랙바

import cv2
import numpy as np

def onChange(value):
    global image, title

    cv2.imshow(title, img)
    r = cv2.getTrackbarPos('R', title)
    g = cv2.getTrackbarPos('G', title)
    b = cv2.getTrackbarPos('B', title)
    img[:] = [b, g, r]

img = np.zeros((300, 512, 3), np.uint8)
title = 'UseCallbackTrackBar'
cv2.namedWindow(title)
# cv2.imshow(title, img)

cv2.createTrackbar('R', title, 0, 255, onChange)
cv2.createTrackbar('G', title, 0, 255, onChange)
cv2.createTrackbar('B', title, 0, 255, onChange)


cv2.waitKey(0)
cv2.destroyAllWindows()
