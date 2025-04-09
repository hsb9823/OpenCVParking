# ------속도 개선---------


# import numpy as np , cv2
# import stackImage as SI
# import filter as F
#
# img = cv2.imread('image/lena.png', cv2.IMREAD_GRAYSCALE) #불러 오려는 영상
#
# data = [ [-1, 0, 0], [0, 1, 0], [0, 0, 0] ]
# mask = np.array(data, np.float32)
#
# dst = F.filter(img, mask)
#
# dst = dst.astype('uint8')
# # output = cv2.filter2D(img, -1 , mask)
# # cv2.imshow('result', dst)
# # cv2.imshow('original', img)
#
# imgStack = SI.stackImages(1, ([[img, dst]]) )
# cv2.imshow('ImageStack', imgStack)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# -----샤프닝------
#cv2.filter2D 사용 연습

# import cv2
# import numpy as np
# import stackImage as SI
#
# img = cv2.imread('image/cards.jpg', cv2.IMREAD_GRAYSCALE)
#
# data = [ [0,-1,0], [-1,5,-1], [0,-1,0] ]
# # data = [ [-1,-1,-1], [-1,9,-1], [-1,-1,-1] ]
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

# ---------로버츠 마스크 filter 함수 사용 -----------

# import cv2
# import numpy as np
# import stackImage as SI
# import filter as F
#
# img = cv2.imread('image/photo.jpg', cv2.IMREAD_GRAYSCALE)
# resize_img = cv2.resize(img, (500, 500))
#
# data1 = [ [0, -1, 0], [0, 1, 0], [0, 0, 0] ]
# data2 = [ [0, 0, -1], [0, 1, 0], [0, 0, 0] ]
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
# cv2.imshow('Roberts Mask', ImgStack)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#---------prewitt mask / filter 함수 사용 -----------

# import cv2
# import numpy as np
# import stackImage as SI
# import filter as F
#
# img = cv2.imread('image/photo.jpg', cv2.IMREAD_GRAYSCALE)
# resize_img = cv2.resize(img, (500,500))
#
# data1 = [ [-1, 0, 1], [-1, 0, 1], [-1, 0, 1] ]
# data2 = [ [-1, -1, -1], [0, 0, 0], [1, 1, 1] ]
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
# cv2.imshow('Prewitt Mask', ImgStack)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#--------- sobel mask / filter 함수 사용 -----------

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

#---------로버츠 마스크 filter2D 함수 사용 -----------

# import cv2
# import numpy as np
# import stackImage as SI
#
# img = cv2.imread('image/photo.jpg', cv2.IMREAD_GRAYSCALE)
# resize_img = cv2.resize(img, (500, 500))
#
# data1 = np.array( [ [0, -1, 0], [0, 1, 0], [0, 0, 0] ] )
# data2 = np.array( [ [0, 0, -1], [0, 1, 0], [0, 0, 0] ] )
#
#
# output1 = cv2.filter2D(resize_img, -1 , data1)
# output2 = cv2.filter2D(resize_img, -1 , data2)
#
# output = abs(output1) + abs(output2)
# ImgStack = SI.stackImages(0.8, ([resize_img, output], [output1, output2]))
# cv2.imshow('Roberts filter2D', ImgStack)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#---------Prewitt mask / filter2D 함수 사용 -----------

# import cv2
# import numpy as np
# import stackImage as SI
#
# img = cv2.imread('image/photo.jpg', cv2.IMREAD_GRAYSCALE)
# resize_img = cv2.resize(img, (500,500))
#
# data1 = np.array( [ [-1, 0, 1], [-1, 0, 1], [-1, 0, 1] ] )
# data2 = np.array( [ [-1, -1, -1], [0, 0, 0], [1, 1, 1] ] )
#
# output1 = cv2.filter2D(resize_img, -1, data1)
# output2 = cv2.filter2D(resize_img, -1, data2)
#
# output = abs(output1) + abs(output2)
# ImgStack = SI.stackImages(0.8, ([resize_img, output], [output1, output2]))
# cv2.imshow('Prewitt Filter2D', ImgStack)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#---------sobel mask / filter2D 함수 사용 -----------

# import cv2
# import numpy as np
# import stackImage as SI
#
# img = cv2.imread('image/photo.jpg', cv2.IMREAD_GRAYSCALE)
# resize_img = cv2.resize(img, (500, 500))
#
# data1 = np.array( [ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1] ] )
# data2 = np.array( [ [1, 2, 1], [0, 0, 0], [-1, -2, -1] ] )
#
# output1 = cv2.filter2D(resize_img, -1, data1)
# output2 = cv2.filter2D(resize_img, -1, data2)
#
# output = abs(output1) + abs(output2)
# ImgStack = SI.stackImages(0.8, ([resize_img, output], [output1, output2]))
# cv2.imshow('sobel', ImgStack)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#=============가우시안 >> 소벨 filter 함수 사용 ================

# import numpy as np
# import cv2
# import stackImage as SI
# import filter as F
#
# img = cv2.imread('image/photo.jpg', cv2.IMREAD_GRAYSCALE)
# resized_img = cv2.resize(img, (500, 500))
#
# #--------------- 가우시안 필터 --------------
# GMask = [ [1/16, 1/8, 1/16], [1/8, 1/4, 1/8], [1/16, 1/8, 1/16] ] # 가우시안 블러링
#
# Gmask1 = np.array(GMask, np.float32)
#
# Gresult = F.filter(img, Gmask1) # 가우시안 필터링 결과
# Gresult = Gresult.astype('uint8') # 가우시간 필터링 결과값 type 변경
# resized_dst1 = cv2.resize(Gresult, (500, 500)) # 가우시안 결과값 창 조절
#
# #=================== 소벨 필터링 ===================
# SMask1 = np.array( [ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1] ] ) # 소벨 마스크
# SMask2 = np.array( [ [1, 2, 1], [0, 0, 0], [-1, -2, -1] ] ) # 소벨 마스크
#
# SMask11 = np.array(SMask1, np.float32)
# SMask22 = np.array(SMask2, np.float32)
#
# Sresult1 = F.filter(resized_dst1, SMask11) # 가우시안 + 소벨 수직 필터링
# Sresult2 = F.filter(resized_dst1, SMask22) # 가우시안 + 소벨 수평 필터링
# Sresult1,Sresult2 = np.array(Sresult1), np.array(Sresult2) # 넘파이 배열로 변경
# sobelresult = cv2.magnitude(Sresult1, Sresult2) # 가우시안 + 소벨 수직 수평 필터링 합침
#
# sobelresult = np.clip(sobelresult, 0, 255).astype('uint8')
# Sresult1 = np.clip(Sresult1, 0, 255).astype('uint8')
# Sresult2 = np.clip(Sresult2, 0, 255).astype('uint8')
#
# ImgStack = SI.stackImages(0.8, ([[resized_img, resized_dst1, sobelresult]] ))
# cv2.imshow('Gaussian >> Sobel Mask', ImgStack)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#=============가우시안 >> 소벨 filter 2D 함수 사용 ================
# import numpy as np
# import stackImage as SI
# import cv2
# black = np.zeros((512,512,3), np.uint8)
# img = cv2.imread('image/photo.jpg', cv2.IMREAD_GRAYSCALE)
# resize_img = cv2.resize(img, (500, 500))
#
# #가우시안 필터링
# GaussianBlur = cv2.GaussianBlur(resize_img, (3,3), 0)
#
# #소벨
# Sdata1 = np.array( [ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1] ] ) #소벨 수직
# Sdata2 = np.array( [ [1, 2, 1], [0, 0, 0], [-1, -2, -1] ] ) #소벨 수평
#
# SMask1 = np.array(Sdata1, np.float32)
# SMask2 = np.array(Sdata2, np.float32)
#
# # 가우시안 필터링한 데이터와 소벨 수직 수평 마스크 필터링
# output1 = cv2.filter2D(GaussianBlur, -1, Sdata1)
# output2 = cv2.filter2D(GaussianBlur, -1, Sdata2)
#
# # 수직 수평 합침
# output = abs(output1) + abs(output2)
#
# # [원본, 가우시안 필터링 처리, 가우시안 >> 소벨]
# # [소벨 + 가우시안 수직 , 소벨 + 가우시안 수평, 빈 창]
# ImgStack = SI.stackImages(0.8, ([resize_img, GaussianBlur, output], [output1, output2, black ]))
# cv2.imshow('G>>S filtering', ImgStack)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()



#=============가우시안 블러 + 소벨 filter2D 함수 사용 ================

import numpy as np
import cv2
import stackImage as SI

img = cv2.imread('image/photo.jpg', cv2.IMREAD_GRAYSCALE)
GaussianBlur = cv2.GaussianBlur(img, (3,3), 0)           # 가우시안 필터링

resize_GaussianBlur = cv2.resize(GaussianBlur, (500, 500))
resize_img = cv2.resize(img, (500, 500))

# ======= 소벨 필터링 ========

# 소벨 마스크
SMask1 = np.array( [ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1] ] ) # 소벨 마스크
SMask2 = np.array( [ [1, 2, 1], [0, 0, 0], [-1, -2, -1] ] ) # 소벨 마스크

SMask11 = np.array(SMask1, np.float32)
SMask22 = np.array(SMask2, np.float32)

#filter2D 사용
output1 = cv2.filter2D(resize_img, -1, SMask11) # 소벨 수직 필터링
output2 = cv2.filter2D(resize_img, -1, SMask22) # 소벨 수평 필터링

Sobel = abs(output1) + abs(output2) # 소벨 필터링 결과

# 가우시안 필터링 처리 + 소벨 필터링 처리 더한 결과
result = abs(resize_GaussianBlur) + abs(Sobel)


# [원본, 가우시안 필터링, 가우시안 필터링 + 소벨]
# [소벨 수직, 소벨 수평, 소벨 결과]
ImgStack = SI.stackImages(0.8, ([[resize_img, resize_GaussianBlur, result], [output1, output2, Sobel ]] ))
cv2.imshow('Gaussian + Sobel Mask', ImgStack)

cv2.waitKey(0)
cv2.destroyAllWindows()