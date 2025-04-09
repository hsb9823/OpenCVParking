# list1 = [1, 2, 3, 4]
# list2 = [1, 1.5, 'a', 'a', '문자열']
# tuple1 = (1, 2)
# tuple2 = (1, 1.5, 'b', 'b', '문자열')
# dict1 = {'name': '배종욱', 'email': 'daum.net'}    # name과 email이라는 키 값 설정
# set1, set2 = set(list2), set(tuple2)
#
# list1[0] = 5
# list2.insert(3, 'b')    # 원소 3번 인덱스에 문자열 b 삽입
#
#
# # tuple1[0] = 5 이다
#
# dict1['email'] = 'naver.com'    # 키 값으로 접근
#
# print('list1', list1, type(list1))
# print('list2', list2, type(list2))
# print('tuple1', tuple1, type(tuple1))
# print('dict1', dict1, type(dict1))
# print('set1', set1, type(set1))
# print('set2', set2, type(set2))
# print('intersection', set1 & set2)

import numpy as np, cv2

img = np.zeros((300, 400), np.uint8)
img [:] = 100

title = 'window'
cv2.namedWindow(title, cv2.WINDOW_NORMAL)
cv2.imshow(title, img)
cv2.waitKey(0)
cv2.destroyAllWindows()