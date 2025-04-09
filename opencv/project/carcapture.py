import cv2

#웹 카메라 캡쳐 변수 cap에 영상을 저장
# num=3
cap = cv2.VideoCapture(0)
#캡쳐/ 변수 ret, img 생성

ret, img = cap.read()

cv2.imshow('capture', img)
cv2.imwrite('images/carcapture/23.jpg', img)
cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()