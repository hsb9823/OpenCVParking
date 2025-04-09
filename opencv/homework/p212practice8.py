import numpy as np
import cv2

image = cv2.imread("image/hsb.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상파일 읽기 오류")

mask = np.zeros(image.shape[:2], np.uint8)  # image와 크기가 같은 검정 영상
center = (380, 250)

cv2.circle(mask, center, 150, (255, 255, 255), -1) # mask라는 검정 영상에 원을 그린다.
dst = cv2.bitwise_and(image, image, mask=mask) # dst값에 비트연산을 하여 저장

cv2.imshow("image", image)
cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()