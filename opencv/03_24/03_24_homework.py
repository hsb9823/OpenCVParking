# 콜백 사용 흑백 트랙바
# 1

import cv2
import numpy as np

def onChange(value):
    global image, title

    image[:] = value
    cv2.imshow(title, image)

image = np.zeros((300,500), np.uint8)

title = 'Trackbar Event'
cv2.imshow(title, image)

cv2.createTrackbar('Brightness', title, 0, 255, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()
