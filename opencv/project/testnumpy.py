import random

# 차량 번호를 입력하면 주차 위치를 알려주는 프로그램


D = {'14모3421': 'A-1', '14모2222': 'A-2', '14모3333': 'A-3', '14모4444': 'A-4', '14모5555': 'A-5',
     '14모6666': 'B-1', '14모7777': 'B-2', '14모8888': 'B-3', '14모9999': 'B-4', '14모1234': 'B-5'}

# 딕셔너리 key value 값 뒤집기
# reverse_D = dict(map(reversed, D.items()))

# print(reverse_D)

for key in D:
    key = input("차량번호를 입력해주세요 : ")
    if key in D:
        print('고객님의 차량은', D[key], '에 있습니다.')
    else:
        print('번호를 찾을수 없습니다. 다시 입력해주세요')

# 주차한 자리에 차량이 들어가면 그 자리에 해당하는 딕셔너리에 차량 번호를 넣음

D = {'1': 'A-1', '2': 'A-2', '3': 'A-3', '4': 'A-4', '5': 'A-5',
     '14모6666': 'B-1', '14모7777': 'B-2', '14모8888': 'B-3', '14모9999': 'B-4', '14모1234': 'B-5'}

a = random.randrange(0,7)
print(a)
D[a] = D.pop('1')
print(D)


# print(plate_classify.a)

# A = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
#
# A = np.array([['1', '2', '3', '4', '5', '6'], ['7', '8', '9', '10', '11', 12]])
#
# A[random.randrange(0,2), random.randrange(0,6)] = plate_classify.carnumber
# print(A)