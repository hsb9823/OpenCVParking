import numpy as np, cv2, math

def draw_houghLines(src, lines, nline):
    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
    min_length = min(len(lines), nline)

    for i in range(min_length):
        rho, radian = lines[i, 0, 0:2]
        a, b = math.cos(radian), math.sin(radian)
        pt = (a * rho, b* rho)
        delta = (-1000 * b, 1000 * a)
        pt1 = np.add(pt, delta).astype('int')
        pt2 = np.subtract(pt, delta).astype('int')
        cv2.linedst, tuple(pt1), tuple(pt2), (0, 255, 0), 2, cv2.LINE_AA)

    return dst

img = cv2.imread('image/cards.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur= cv2.GaussianBlur(imgray, (5, 5), 2, 2)
canny = cv2.Canny(blur, 50, 150, 5)

cv2.imshow('imgray', imgray)
cv2.imshow('canny', canny)

lines = cv2.HoughLines()