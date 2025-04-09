import cv2

imgfile = 'hsb.jpg'
img = cv2.imread(imgfile, cv2.IMREAD_UNCHANGED)

cv2.namedWindow('Capture', cv2.WINDOW_NORMAL)   # 윈도우 크기 조정 가능
# cv2.namedWindow('Capture', cv2.WINDOW_AUTOSIZE)   # 표시된 행렬의 크기에 맞춰 윈도우 크기 자동 조정
cv2.moveWindow('Capture', 400, 150)
cv2.resizeWindow('Capture', 300, 300)
cv2.imshow('Capture', img)
cv2.waitKey(0)
cv2.destroyAllWindows()