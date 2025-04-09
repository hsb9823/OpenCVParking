# matplottest

# import numpy as np
# from matplotlib import pyplot as plt
#
# x = np.arange(0,20, 0.01)
# y = x*x + 4*x + 4
#
# plt.plot(x, y)
# plt.show()

# --------------------------------------------- #
# image test

# import cv2
# from matplotlib import pyplot as plt
#
# path = 'image/lena.png'
# img = cv2.imread(path)
# plt.axis('off')
# plt.imshow(img)
# plt.show()

# --------------------------------------------- #
# image test2

# import cv2
# from matplotlib import pyplot as plt
#
# path = 'image/banana.jpg'
# img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
#
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.xticks([])
# plt.yticks([])
# plt.title('banana')
# plt.show()

# --------------------------------------------- #
# image test3

# import cv2
# import numpy as np
#
# img = cv2.imread('image/lambo.png')
# print(img.shape)
#
# imgResize = cv2.resize(img, (320, 240))
# print(imgResize.shape)
#
# cv2.imshow('Image', img)
# cv2.imshow('Image Resize', imgResize)
#
# cv2.waitKey()
# cv2.destroyAllWindows()

# --------------------------------------------- #
# stackImage.py파일을 import하여 si라는 이름으로 정의하고, 내부에 정의된 함수 stackImages를 불러와 짧은 코드로 똑같이 동작

import cv2
import stackImage as si

img = cv2.imread('image/lena.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

stackimg = si.stackImages(0.5, ([img, imgGray]))
cv2.imshow('test', stackimg)

cv2.waitKey()
cv2.destroyAllWindows()