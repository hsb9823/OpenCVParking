import numpy as np
import cv2

drawing = False
ix, iy, w, h = -1, -1, -1, -1

def ROI(event, x, y, flags, param):
    global drawing, ix, iy, img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True

        ix = x
        iy = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_draw = img.copy()
            cv2.rectangle(img_draw, (ix, iy), (x,y), (0,0, 255), 2)
            cv2.imshow('img', img_draw)
    elif event == cv2.EVENT_LBUTTONUP:
        if drawing:
            drawing = False

            img