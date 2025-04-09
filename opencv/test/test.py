# import numpy as np, cv2
# img = np.zeros((300, 400, 3), np.uint8)
# img[:] = (255, 255, 255)
#
# pt1, pt2 = (50, 130), (200, 300)
#
# cv2.line(img, pt1, (100,200), (255, 0, 0))
# cv2.line(img, pt2, (100,100), (255, 0, 0))
# cv2.rectangle(img, pt1, pt2, (255, 0, 255))
# cv2.rectangle(img, pt1, pt2, (0, 0, 255))
#
# title = 'Line & Rectangle'
#
# cv2.namedWindow(title)
# cv2.imshow(title, img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 7번
# import numpy as np, cv2
#
# def onMouse(event, x, y, flags, param):
#     global title, pt
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(img, pt, 5, 100, 1)
#         pt = (-1, -1)
#     elif event == cv2.EVENT_RBUTTONDOWN:
#         cv2.rectangle(img, pt, pt+(30,30), 100, 2)
#         cv2.imshow(title, img)
#         pt = (-1, -1)
#
# img = np.ones((300,300), np.uint8) * 255
#
# pt = (-1, -1)
# title = 'Draw Event'
# cv2.namedWindow(title)
# cv2.imshow(title, img)
# cv2.setMouseCallback(title, onMouse)
# cv2.waitKey()
# cv2.destroyAllWindows()


# 9번
# import numpy as np, cv2
# img = np.zeros((600, 400, 3), np.uint8)
# img[:] = (255, 255, 255)
#
#
# cv2.rectangle(img, (100,100,200,300), (0, 0, 255), cv2.FILLED)
#
# title = 'Line & Rectangle'
#
# cv2.namedWindow(title)
# cv2.imshow(title, img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 9번 2

# import numpy as np, cv2
#
# # 600행, 400열의 윈도우를 만들고(3채널 흰 영상)
# img = np.full((600, 400, 3), (255, 255, 255), np.uint8)
# title = 'test'
#
# # 영상의 (100, 100) 좌표에 200x300 크기의 빨간색 사각형을 그리시오
# pt1, pt2 = (100, 100), (300, 400)
# red = (0, 0, 255)
# cv2.rectangle(img, pt1, pt2, red, -1)
#
# cv2.imshow(title, img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#
# # 10번
# import numpy as np, cv2
#
# def onMouse(event, x, y, flags, param):
#     global title
#
#     # 마우스 오른쪽 버튼 클릭 시
#     if event == cv2.EVENT_RBUTTONDOWN:
#         # 클릭 좌표에서 반지름이 20인 원 그리기
#         cv2.circle(img, (x, y), 20, (0, 0, 255), 2) # 두께가 2인 빨간 원
#     # 마우스 왼쪽 버튼 클릭 시
#     elif event == cv2.EVENT_LBUTTONDOWN:
#         # 크기 30x30인 사각형 그리기
#         cv2.rectangle(img, (x, y), (x+30, y+30), (255, 0, 0), 2) # 두께가 2인 파란 사각형
#
#     cv2.imshow(title, img)
#
# img = np.full((400, 300, 3), (255, 255, 255), np.uint8)
# title = 'test'
# cv2.imshow(title, img)
# cv2.setMouseCallback(title, onMouse)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#6장 8번
# import numpy as np, cv2
#
# image1 = cv2.imread("image/add1.jpg", cv2.IMREAD_GRAYSCALE)
# image2 = cv2.imread("image/add2.jpg", cv2.IMREAD_GRAYSCALE)
#
# title = ' dst'
# a, b = 0.6, 0.4                                                       # 곱샘 비율
#
# image3 = cv2.addWeighted(image1, a, image2, b, 0)                     # 두영상 비율에 따른 더하기
#
# width, height = image1.shape                                          # image1의 가로, 세로 길이
# dst = np.zeros((width, height*3), np.uint8)                           # image1의 가로, 세로 * 3의 배열 생성
# dst[0:height, 0:width] = image1[0:height, 0:width]                    # 배열의 맨 앞에 image1 넣기
# dst[:, width*2:] = image2[0:height, 0:width]                          # 배열의 맨 뒤에 image2 넣기
# dst[0:height, width:width*2] = image3[0:height, 0:width]              # 배열의 가운데에 image3 넣기
#
# cv2.imshow(title, dst)
# cv2.waitKey(0)

# 6장 9번
#
# import numpy as np, cv2
#
# def bar(value) :
#     global alpha, beta, title, image1, image2, dst
#
#     # alpha, bete값 구하기
#     alpha = cv2.getTrackbarPos('image1', title) / 100
#     beta = cv2.getTrackbarPos('image2', title) / 100
#
#     # alpha, beta값으로 영상 합성하기
#     image3 = cv2.addWeighted(image1, alpha, image2, beta, 0)  # 두영상 비율에 따른 더하기
#     dst[0:h, w:w*2] = image3[0:h, 0:w]                        # 배열의 가운데에 image3 넣기
#
#     cv2.imshow(title, dst)
#
#
# # 영상 읽기
# image1 = cv2.imread("image/add1.jpg", cv2.IMREAD_GRAYSCALE)
# image2 = cv2.imread("image/add2.jpg", cv2.IMREAD_GRAYSCALE)
# if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생")
# title = ' dst'
#
# # 영상 합성
# alpha, beta = 0.6, 0.4                                       # 곱샘 비율
# image3 = cv2.addWeighted(image1, alpha, image2, beta, 0)     # 두영상 비율에 따른 더하기
#
# # 영상 3개가 들어갈 배열 생성하고 영상 넣기
# w, h = image1.shape                                          # image1의 가로, 세로 길이
# dst = np.zeros((w, h*3), np.uint8)                           # image1의 가로, 세로 * 3의 배열 생성
# dst[0:h, 0:w] = image1[0:h, 0:w]                             # 배열의 맨 앞에 image1 넣기
# dst[:, w*2:] = image2[0:h, 0:w]                              # 배열의 맨 뒤에 image2 넣기
# dst[0:h, w:w*2] = image3[0:h, 0:w]                           # 배열의 가운데에 image3 넣기
#
# cv2.imshow(title, dst)
#
# # alpha, beta값을 조절할 트랙바 달기
# cv2.createTrackbar('image1', title, 50, 100, bar)
# cv2.createTrackbar('image2', title, 50, 100, bar)
#
# cv2.waitKey(0)

