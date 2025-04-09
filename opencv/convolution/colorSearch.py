import cv2
import numpy as np
import stackImage as SI

img = cv2.imread('image/redcircle.jpg', cv2.COLOR_BGR2GRAY)

def empty(a):
    pass

titles = "TrackBars"
cv2.namedWindow(titles)
cv2.resizeWindow(titles,640,240)
cv2.createTrackbar("Hue Min",titles,0,179,empty)
cv2.createTrackbar("Hue Max",titles,19,179,empty)
cv2.createTrackbar("Sat Min",titles,110,255,empty)
cv2.createTrackbar("Sat Max",titles,240,255,empty)
cv2.createTrackbar("Val Min",titles,153,255,empty)
cv2.createTrackbar("Val Max", titles,255,255,empty)
 
while True:
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min",titles)
    h_max = cv2.getTrackbarPos("Hue Max", titles)
    s_min = cv2.getTrackbarPos("Sat Min", titles)
    s_max = cv2.getTrackbarPos("Sat Max", titles)
    v_min = cv2.getTrackbarPos("Val Min", titles)
    v_max = cv2.getTrackbarPos("Val Max", titles)

 
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)
 
 
    # cv2.imshow("Orig",img)
    # cv2.imshow("HSV",imgHSV)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Result", imgResult)

    imgStack = SI.stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
    cv2.imshow("Stacked Image", imgStack)
 
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
