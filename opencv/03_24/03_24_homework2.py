# 콜백 사용 X 흑백 트랙바

import cv2
import numpy as np

def nothing(x):
    pass

title = 'Trackbar Event'
image = np.zeros((300,500), np.uint8)
cv2.namedWindow(title)
cv2.createTrackbar('Brightness', title, 0, 255, nothing)

while(1):
    cv2.imshow(title, image)
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break
    value = cv2.getTrackbarPos('Brightness', title)
    image[:] = value

cv2.destroyAllWindows()
