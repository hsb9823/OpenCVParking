# import numpy as np
# import cv2
#
# import matplotlib.pyplot as plt  # 히스토그램 plot
#
# img = cv2.imread('image/lambo.png', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('test', img)
# hist = np.zeros(256, np.int32)  # 히스토그램 – gray 256 level
#
# # for y in range(img.shape[0]):
# #         for x in range(img.shape[1]):
# #                 k = img[y][x]
# #                 hist[k] = hist[k]+1
#
# # ------------------------------------------------------------------- #
#
# cv2.calcHist(img, [0], None, [256], [0, 256])
# # img.flatten() or img.ravel() : 다차원의 배열을 1차원으로 변경
# plt.hist(img.ravel(), 256, [0, 256])
#
# plt.plot(hist)
# plt.xlim(0)
# plt.show()
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 컬러 히스토그램

# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
#
# img = cv2.imread('image/lambo.png')
# cv2.imshow('colorhistgram', img)
# color = ('b', 'g', 'r')
#
# for i, col in enumerate(color):
#         histr = cv2.calcHist([img], [i], None, [256], [0, 256])
#         plt.plot(histr, color=col)
#         plt.xlim([0,256])
#
# plt.show()


# 히스토그램 스트레칭

# import numpy as np, cv2
# import matplotlib.pyplot as plt
# def search_idx(hist, bias = 0):
#         for i in range(hist.shape[0]):
#                 idx = np.abs(bias-i)
#                 if hist[idx] > 0: return idx
#         return -1
#
# img = cv2.imread('image/lena.png', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('img', img)
# img_str = img.copy()
# hist = cv2.calcHist([img], [0], None, [256],[0, 256])
#
# #stretching
#
# low = search_idx(hist, 0)
# high = search_idx(hist, 255)
# for y in range(img.shape[0]):
#         for x in range(img.shape[1]):
#
#                 img_str[y][x] = ((img[y][x]-low)/(high-low))*255
#
# cv2.imshow('stretch', img_str)
# hist1 = cv2.calcHist([img_str], [0], None, [256],[0, 256])
#
# plt.hist(img.ravel(), 256, [0,256])
# plt.hist(img_str.ravel(), 256, [0,256])
# plt.show()
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 히스토그램

import numpy as np
import cv2
import matplotlib.pyplot as plt

# 이미지 불러오기
img = cv2.imread('image/lena.png', cv2.IMREAD_COLOR)
cv2.imshow('lena original', img)
# 삽입 이미지 히스토그램 계산

histogram = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.hist(img.ravel(), 256, [0, 256])

img_equal = img.copy()


# allocate for the histogram

hist = sum_hist = np.zeros(256, np.int32)

# 히스토그램 계산

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        k = img[y][x]
        hist[k] = hist[k]+1


sum = 0
for i in range(hist.size):
    sum = sum + hist[i] / (img.shape[0] * img.shape[1])
    sum_hist[i] = (int)((sum*255.0) + 0.5)


#변환
for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        img_equal[y][x] = np.int8(sum_hist[img[y][x]])


cv2.imshow('equalization', img_equal)


histogram1 = cv2.calcHist([img_equal], [0], None, [256], [0, 256])
plt.hist(img_equal.ravel(), 256, [0, 256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()