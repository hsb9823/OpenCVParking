import numpy as np
import cv2
import stackImage as SI

def nothing(x):
    pass
cv2.namedWindow('morphology')
cv2.createTrackbar('th', 'morphology', 0, 255, nothing)
cv2.setTrackbarPos('th', 'morphology', 100)

img = cv2.imread('image/redcircle.jpg', cv2.IMREAD_GRAYSCALE)

while(True):
    kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    kernel3 = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
    kernel4 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    kernel5 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
    kernel6 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
    kernel7 = cv2.getStructuringElement(cv2.MORPH_CROSS, (3,3))
    kernel8 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,5))
    kernel9 = cv2.getStructuringElement(cv2.MORPH_CROSS, (7,7))

    low = cv2.getTrackbarPos('th', 'morphology')
    ret, th1 = cv2.threshold(img, low, 255, cv2.THRESH_BINARY_INV)
    rect33 = cv2.dilate(th1, kernel1, iterations=2)
    rect55 = cv2.dilate(th1, kernel2, iterations=2)
    rect77 = cv2.dilate(th1, kernel3, iterations=2)
    ellipse33 = cv2.dilate(th1, kernel4, iterations=2)
    ellipse55 = cv2.dilate(th1, kernel5, iterations=2)
    ellipse77 = cv2.dilate(th1, kernel6, iterations=2)
    cross33 = cv2.dilate(th1, kernel7, iterations=2)
    cross55 = cv2.dilate(th1, kernel8, iterations=2)
    cross77 = cv2.dilate(th1, kernel9, iterations=2)

    imgstack = SI.stackImages(0.4, ([rect33, rect55, rect77], [ellipse33, ellipse55, ellipse77], [cross33, cross55, cross77]))
    cv2.imshow('morphology', imgstack)

    if cv2.waitKey(1) & 0xFF == 27:
        break

# cv2.waitKey(0)
# cv2.destroyAllWindows()
#


