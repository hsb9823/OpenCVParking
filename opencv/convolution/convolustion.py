# import cv2
# import numpy as np
#
# img = cv2.imread('image/cards.jpg', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('img', img)
#
# kernel = np.array([ [0,0,0], [0,1,0], [0,0,0] ])
#
# r, c = img.shape
# img_result = img.copy()
#
# for y in range(r) :
#     for x in range(c):
#         sum = 0
#         for a in [-1, 0 ,1]:
#             for b in [-1, 0, 1]:
#                 if y+a <= 0 or y+a >= r or x+b <= 0 or x+b >= c:
#                     continue
#
#                 sum += img[y+a][x+b]*kernel[a+1][b+1]
#
#                 if sum < 0 : img_result[y][x] = 0
#                 elif sum > 255 : img_result[y][x] = 255
#                 else : img_result[y][x] = np.int8(sum)
#
# cv2.imshow('result', img_result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# ------속도 개선---------


import numpy as np , cv2
import stackImage as SI
import filter as F

img = cv2.imread('image/lena.png', cv2.IMREAD_GRAYSCALE) #불러 오려는 영상

data = [ [1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9] ] # 블러링
# data = [ [-1, 0, 0], [0, 1, 0], [0, 0, 0] ] # 로버츠 마스크
mask = np.array(data, np.float32)

dst = F.filter(img, mask)
dst = dst.astype('uint8')
# cv2.imshow('result', dst)
# cv2.imshow('original', img)

imgStack = SI.stackImages(1, ([[img, dst]]) )
cv2.imshow('ImageStack', imgStack)

cv2.waitKey(0)
cv2.destroyAllWindows()


# -----샤프닝------
#cv2.filter2D 사용 연습

# import cv2
# import numpy as np
# import stackImage as SI
#
# img = cv2.imread('image/cards.jpg', cv2.IMREAD_GRAYSCALE)
#
# data = [ [0,-1,0], [-1,5,-1], [0,-1,0] ]
# data = [ [-1,-1,-1], [-1,9,-1], [-1,-1,-1] ]
# mask = np.array(data, np.float32)       # 데이터 형태 uint8 >>> float32
#
# output = cv2.filter2D(img, -1 , mask)
# # cv2.imshow('original', img)
# # cv2.imshow('3x3 filter', output)
#
# imgStack = SI.stackImages(0.8, ([[img, output]]) )
# cv2.imshow('ImageStack', imgStack)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# ------에지 검출 -------

# import cv2
# import numpy as np
# import stackImage as SI
# import filter as F
#
# img = cv2.imread('image/photo.jpg', cv2.IMREAD_GRAYSCALE)
# resize_img = cv2.resize(img, (500,500))
#
# horizonMask = [ [-1, -2, -1], [0, 0, 0], [1, 2, 1] ]
# verticalMask = [ [1, 0, -1], [2, 0, -2], [1, 0, -1] ]
#
# mask1 = np.array(horizonMask, np.float32)
# mask2 = np.array(verticalMask, np.float32)
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
# cv2.imshow('Sobel Mask', ImgStack)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

