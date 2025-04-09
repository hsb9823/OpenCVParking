# # ============= 라플라시안 함수이용 ============

# import cv2
# import numpy as np
#
# img = cv2.imread('image/sudoku.png', cv2.IMREAD_GRAYSCALE)
# laplacian = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
# Lap = cv2.convertScaleAbs(laplacian)
#
# cv2.imshow('Laplacian', Lap)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ============= filter 사용 Laplacian edge 검출============

# import cv2
# import numpy as np
# import stackImage as SI
# import filter as F
#
# img = cv2.imread('image/sudoku.png', cv2.IMREAD_GRAYSCALE)
# resize_img = cv2.resize(img, (500, 500))
#
# # 4방향 마스크
# # data1 = [ [0, -1, 0], [-1, 4, -1], [0, -1, 0] ]
# # data2 = [ [0, 1, 0], [1, -4, 1], [0, 1, 0] ]
#
# # 8방향 마스크
# data1 = [ [-1, -1, -1], [-1, 8, -1], [-1, -1, -1] ]
# data2 = [ [1, 1, 1], [1, -8, 1], [1, 1, 1] ]
#
#
# mask1 = np.array(data1, np.float32)
# mask2 = np.array(data2, np.float32)
#
# dst1 = F.filter(resize_img, mask1)
# dst2 = F.filter(resize_img, mask2)
# dst1, dst2 = np.array(dst1), np.array(dst2)
# dst = cv2.magnitude(dst1, dst2)
#
# dst = np.clip(dst, 0, 255).astype('uint8')
# dst1 = np.clip(dst1, 0, 255).astype('uint8')
# dst2 = np.clip(dst2, 0, 255).astype('uint8')
#
# ImgStack = SI.stackImages(0.8, ([resize_img, dst], [dst1, dst2]))
# cv2.imshow('Laplacian Mask', ImgStack)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ============= filter2D 사용 Laplacian edge 검출============

import cv2
import numpy as np
import stackImage as SI

img = cv2.imread('image/sudoku.png', cv2.IMREAD_GRAYSCALE)
resize_img = cv2.resize(img, (500, 500))

# 4방향 마스크
# data1 = np.array( [ [0, -1, 0], [-1, 4, -1], [0, -1, 0] ] )
# data2 = np.array( [ [0, 1, 0], [1, -4, 1], [0, 1, 0] ] )

#8방향 마스크
data1 = np.array( [ [-1, -1, -1], [-1, 8, -1], [-1, -1, -1] ] )
data2 = np.array( [ [1, 1, 1], [1, -8, 1], [1, 1, 1] ])

output1 = cv2.filter2D(resize_img, -1 , data1)
output2 = cv2.filter2D(resize_img, -1 , data2)

output = abs(output1) + abs(output2)
ImgStack = SI.stackImages(0.8, ([resize_img, output], [output1, output2]))
cv2.imshow('Laplacian filter2D', ImgStack)

cv2.waitKey(0)
cv2.destroyAllWindows()