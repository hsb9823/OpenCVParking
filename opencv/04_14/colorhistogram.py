import numpy as np
import cv2
import matplotlib.pyplot as plt
import stackImage as si

# 이미지 불러오기
img = cv2.imread('image/lena.png', cv2.IMREAD_COLOR)
cv2.imshow('lena original', img)

img_b, img_g, img_r = cv2.split(img)   # 이미지 BGR 성분으로 나눔
# cv2.imshow('b', img_b)
# cv2.imshow('g', img_g)
# cv2.imshow('r', img_r)
# 삽입 이미지 히스토그램 계산

histogram1 = cv2.calcHist([img_b], [0], None, [256], [0, 256])
histogram2 = cv2.calcHist([img_g], [0], None, [256], [0, 256])
histogram3 = cv2.calcHist([img_r], [0], None, [256], [0, 256])
plt.hist(img_b.ravel(), 256, [0, 256])
plt.hist(img_g.ravel(), 256, [0, 256])
plt.hist(img_r.ravel(), 256, [0, 256])


img_equal1 = img_b.copy()
img_equal2 = img_g.copy()
img_equal3 = img_r.copy()

# allocate for the histogram

hist1 = sum_hist1 = np.zeros(256, np.int32)
hist2 = sum_hist2 = np.zeros(256, np.int32)
hist3 = sum_hist3 = np.zeros(256, np.int32)

# 히스토그램 계산

for y in range(img_b.shape[0]):
    for x in range(img_b.shape[1]):
        k = img_b[y][x]
        hist1[k] = hist1[k]+1
for y in range(img_g.shape[0]):
    for x in range(img_g.shape[1]):
        k = img_g[y][x]
        hist2[k] = hist2[k]+1
for y in range(img_r.shape[0]):
    for x in range(img_r.shape[1]):
        k = img_r[y][x]
        hist3[k] = hist3[k]+1


sum = 0
for i in range(hist1.size):
    sum = sum + hist1[i] / (img_b.shape[0] * img_b.shape[1])
    sum_hist1[i] = (int)((sum*255.0) + 0.5)

for i in range(hist2.size):
    sum = sum + hist2[i] / (img_g.shape[0] * img_g.shape[1])
    sum_hist2[i] = (int)((sum*255.0) + 0.5)

for i in range(hist3.size):
    sum = sum + hist3[i] / (img_r.shape[0] * img_r.shape[1])
    sum_hist3[i] = (int)((sum*255.0) + 0.5)

#변환
for y in range(img_b.shape[0]):
    for x in range(img_b.shape[1]):
        img_equal1[y][x] = np.int8(sum_hist1[img_b[y][x]])

for y in range(img_g.shape[0]):
    for x in range(img_g.shape[1]):
        img_equal2[y][x] = np.int8(sum_hist2[img_g[y][x]])

for y in range(img_r.shape[0]):
    for x in range(img_r.shape[1]):
        img_equal3[y][x] = np.int8(sum_hist3[img_r[y][x]])


histogram1 = cv2.calcHist([img_equal1], [0], None, [256], [0,256])
histogram2 = cv2.calcHist([img_equal2], [0], None, [256], [0,256])
histogram3 = cv2.calcHist([img_equal3], [0], None, [256], [0,256])

plt.hist(img_equal1.ravel(), 256, [0, 256])
plt.hist(img_equal2.ravel(), 256, [0, 256])
plt.hist(img_equal3.ravel(), 256, [0, 256])



# cv2.imshow('equalization channel b', img_equal1)
# cv2.imshow('equalization channel g', img_equal2)
# cv2.imshow('equalization channel r', img_equal3)
Final_img = cv2.merge([img_equal1, img_equal2, img_equal3]) # 평활화 한 각각의 BGR 채널을 merge하여 합침
cv2.imshow('Final equalization b+g+r', Final_img)

stackimg = si.stackImages(0.5, ([img_b, img_g, img_r], [img_equal1, img_equal2, img_equal3]))
cv2.imshow('stack', stackimg)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()