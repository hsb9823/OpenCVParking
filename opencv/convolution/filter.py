import numpy as np , cv2

#define filter() 함수 제작

def filter(img, mask):
    r, c = img.shape[:2]
    dst = np.zeros((r, c), np.float32)    #이미지의 row colum

    ycenter, xcenter = mask.shape[0]//2, mask.shape[1]//2

    # 컨벌루션
    for i in range(ycenter, r - ycenter):
        for j in range(xcenter, c -xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1
            x1, x2 = j - xcenter, j + xcenter + 1
            roi = img[y1:y2, x1:x2].astype('float32')

            tmp = cv2.multiply(roi, mask)
            # dst[i, j] = cv2.sumElems(tmp)[0]
            tmp = cv2.sumElems(tmp)[0]

            if tmp < 0: dst[i, j] = 0
            elif tmp > 255: dst[i, j] = 255
            else: dst[i, j] = tmp

    return dst