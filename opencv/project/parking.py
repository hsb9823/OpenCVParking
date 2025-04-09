import plate_classify
from classify_numbers import *
import keyboard
import random


parking() # classify_numbers 내부 parking 함수 실행

D = {1: 'A-1', 2: 'A-2', 3: 'A-3', 4: 'A-4', 5: 'A-5', 6: 'A-6',
     7: 'B-1', 8: 'B-2', 9: 'B-3', 10: 'B-4', 11: 'B-5', 12: 'B-6'}

print('-------------------------------------------------')

a = random.randint(1, 13)
print("차량 위치 임의 배정 :", a)

D[plate_classify.carnumber] = D.pop(a)
print("주차 위치가 저장된 딕셔너리 출력 :\n" ,D)
print("주차 위치 표시 :",D[plate_classify.carnumber])

for key in D:
    key = input("차량번호를 입력해주세요 : ")
    if key in D:
        print('고객님의 차량은', D[key], '에 있습니다.')
        break
    else:
        print('번호를 찾을수 없습니다. 다시 입력해주세요')

