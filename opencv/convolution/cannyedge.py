import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('cannyedge')
cv2.createTrackbar('th1', 'cannyedge', 0, 255, nothing)
cv2.setTrackbarPos('th1', 'cannyedge', 100)
cv2.createTrackbar('th2', 'cannyedge', 0, 255, nothing)
cv2.setTrackbarPos('th2', 'cannyedge', 100)

cap = cv2.VideoCapture(0)
ret, img = cap.read()
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

while(True):
    pos1 = cv2.getTrackbarPos('th1', 'cannyedge')
    pos2 = cv2.getTrackbarPos('th2', 'cannyedge')

    img_edge = cv2.Canny(img_gray, pos1, pos2)

    cv2.imshow('original', img_gray)
    cv2.imshow('Canny edge', img_edge)

    if cv2.waitKey(1) & 0xFF == 27:
        break
