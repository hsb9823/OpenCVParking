import numpy as np
import cv2
logo = cv2.imread("image/logo.jpg", cv2.IMREAD_COLOR)

if logo is None : raise Exception("영상파일 읽기 오류")
# bgr = cv2.split(logo)
blue, green, red = cv2.split(logo)

img1 = np.zeros_like(green) # [0,255,0] green 리스트를 [0, 0, 0]으로 바꿔줌으로써 검은 화면을 만든다.
blue_img = cv2.merge([blue, img1, img1])   #merge함수를 이용, split으로 나눈 3채널을 합친다.
green_img = cv2.merge([img1, green, img1])
red_img = cv2.merge([img1, img1, red])

print("red_img = \n%s" % red_img) #생성된 배열 확인
print("img1 = \n%s" % img1) # img1의 배열 확인

cv2.imshow('black', img1)  # show함수를 통해 img 리스트 내부 요소가 0으로 변경 되어 검은 화면을 만들었음을 확인
cv2.imshow('logo', logo)
cv2.imshow('blue_img', blue_img)
cv2.imshow('green_img', green_img)
cv2.imshow('red_img', red_img)
cv2.waitKey(0)
cv2.destroyAllWindows()