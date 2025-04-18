# import cv2
# import numpy as np
# import stackImage
# cap = cv2.VideoCapture(0)
#
# while(1):
#
#     ret, img = cap.read()
#     if ret == False : break
#
#     # img = cv2.imread('image/cocacola.png')
#     img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#
#     lower_red = (150, 50, 50)
#     upper_red = (190, 255, 255)
#
#     img_mask = cv2.inRange(img_hsv, lower_red, upper_red)
#
#     img_result = cv2.bitwise_and(img, img, mask=img_mask)
#
#     # cv2.imshow('original img', img)
#     # cv2.imshow('mask', img_mask)
#     # cv2.imshow('img_result', img_result)
#     imgStack = stackImage.stackImages(0.6, ([img, img_mask, img_result]))
#     cv2.imshow("Stacked Image", imgStack)
#
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#
# cv2.destroyAllWindows()



import numpy as np
import cv2
import stackImage

cap = cv2.VideoCapture(0)
ret, img = cap.read()

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

    cv2.imshow("Original", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)

    imgStack = stackImage.stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
    cv2.imshow("Stacked Image", imgStack)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()