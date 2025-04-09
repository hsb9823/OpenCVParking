# # 트랙바 이벤트 제어 1
#
# import cv2
# import numpy as np
#
#
# def onChange(value):
#     global image, title
#
#     image[:] = value
#     cv2.imshow(title, image)
#
#
# image = np.zeros((300, 500), np.uint8)
#
# title = 'Trackbar Event'
# cv2.imshow(title, image)
# cv2.createTrackbar('Brightness', title, 0, 255, onChange)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 트랙바 이벤트 제어 2 callback 함수 사용 X 

import cv2
import numpy as np

def nothing(x):
    pass

title = 'Trackbar Event'
image = np.zeros((300, 500), np.uint8)
cv2.namedWindow(title)
cv2.createTrackbar('Brightness', title, 0, 255, nothing)  # 콜백함수 대신 while문으로 처리

while (1):
    cv2.imshow(title, image)
    k = cv2.waitKey(1) & 0xff
    if k == 27:  # esc누르면 window 창 탈출 // 아무키 누르고 탈출을 원하면 cv2.waitKey(0)으로 변경
        break

    value = cv2.getTrackbarPos('Brightness', title)
    image[:] = value

cv2.destroyAllWindows()
