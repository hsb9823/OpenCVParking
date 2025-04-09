# import cv2
#
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, img = cap.read()
#     if ret == False : break
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     cv2.imshow('color', img)
#     cv2.imshow('gray', img_gray)
#
#     if cv2.waitKey(1) & 0xff == 27:
#         break
#
# print(img.shape)
# print(img_gray.shape)
#
# cap.release()
# cv2.destroyAllWindows()

 # ------------------------------------------------------- #

# import cv2
# import numpy as np
#
# img = cv2.imread('image/cocacola.png')
#
# img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
# lower_red = (161, 155, 84)
# upper_red = (179, 255, 255)
# img_mask = cv2.inRange(img_hsv, lower_red, upper_red)
# img_result = cv2.bitwise_and(img, img, mask=img_mask)
#
# cv2.imshow('img', img)
# cv2.imshow('img_mask', img_mask)
# cv2.imshow('img_result', img_result)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# -------------------------------------------------------------------#
import numpy as np
import cv2
import stackImage

img = cv2.imread('image/redcircle.jpg', cv2.COLOR_BGR2GRAY)
# cap = cv2.VideoCapture(0)
# ret, img = cap.read()

def empty(a):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 240, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 153, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    # print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow("Original", img)
    # cv2.imshow("HSV", imgHSV)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Result", imgResult)

    imgStack = stackImage.stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
    cv2.imshow("Stacked Image", imgStack)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# cap.release()
cv2.destroyAllWindows()




# import numpy as np
# import cv2
# import stackImage as SI
# img = cv2.imread('image/cards.jpg', cv2.IMREAD_GRAYSCALE)
# ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# ret, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# ret, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# ret, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# ret, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
# stackImage = SI.stackImages(0.6, ([img, thr1, thr2], [thr3, thr4, thr5] ))
# cv2.imshow('ImageStack', stackImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# import stackImage as SI
#
# def nothing(x):
#     pass
#
# cv2.namedWindow('original')
# cv2.namedWindow('thr1')
# cv2.namedWindow('thr2')
# cv2.namedWindow('thr3')
# # cv2.createTrackbar('t', 'B', 0, 255, nothing)
# # cv2.setTrackbarPos('t', 'B' ,127)
#
# cap = cv2.VideoCapture(0)
#
# while(1):
#
#     ret, img = cap.read()
#     if ret == False :
#         continue
#
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # pos = cv2.getTrackbarPos('t', 'B')
#     ret, thr1 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
#     thr2 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
#     thr3 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 5)
#
#
#     cv2.imshow('original', img_gray)
#     cv2.imshow('thr1', thr1)
#     cv2.imshow('thr2', thr2)
#     cv2.imshow('thr3', thr3)
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()



# # Adaptive Threshold 예제
# import numpy as np
# import cv2
# import stackImage as SI
# img = cv2.imread('dave.jpg', cv2.IMREAD_GRAYSCALE)
# ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# thr2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,
# 11, 5)
# thr3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
# cv2.THRESH_BINARY, 11,5)
# imgStack = SI.stackImages(0.6, ([img, thr1], [thr2, thr3] ))
# cv2.imshow('ImageStack', imgStack)
# cv2.waitKey(0)
# cv2.destroyAllWindows()







