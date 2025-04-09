import cv2


draw = False
xx, yy = -1, -1


def mouse_callback(event, x, y, flags, param):
    global xx, yy, draw

    img_result = img.copy()

    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        xx, yy = x, y
        cv2.imshow("img", img_result)

    elif event == cv2.EVENT_MOUSEMOVE:

        if draw:
            cv2.rectangle(img_result, (xx, yy), (x, y), (255, 255, 255), 1)
            cv2.imshow("img", img_result)

    elif event == cv2.EVENT_LBUTTONUP:

        draw = False

        roi = img[yy:y, xx:x]

        img_result[yy:y, xx:x] = roi
        cv2.imshow("img", img_result)
        cv2.imshow("roi", roi)


img = cv2.imread('image/hsb.jpg', cv2.IMREAD_COLOR )

cv2.imshow("img", img)
cv2.setMouseCallback('img', mouse_callback)
cv2.waitKey(0)
cv2.destroyAllWindows()