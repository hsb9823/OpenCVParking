# while(1):
#     print('동전으로 바꿔드립니다.')
#     print('금액을 입력하세요.')
#     money, c500, c100, c50 = 0, 0, 0, 0
#     money = int(input())
#
#     c500 = money//500
#     money %= 500
#
#     c100 = money//100
#     money %= 100
#
#     c50 = money//50
#     money %= 50
#
#     print('500원 = %d개' %c500)
#     print('100원 = %d개' %c100)
#     print('50원 = %d개' %c50)
#     print('잔돈 = %d원' %money)

# score_list = []
# students = ['A', 'B', 'C', 'D', 'E']
# total = 0
#
# print("본인의 성적을 입력하세요.")
# my_score = int(input())
#
# for i in students:
#     print(i, "학생 성적을 입력하시오 : ")
#     score_list.append(int(input()))
#
# for j in score_list:
#     total += j
#
# mean = total / 5
# print("5명의 학생 평균은", mean, "입니다.")
#
# if my_score >= mean :
#     print("귀하의 성적은", my_score, "입니다.")
#     print("귀하의 성적은 평균 이상입니다!")
# elif my_score < mean :
#     print("귀하의 성적은", my_score, "입니다.")
#     print("귀하의 성적은 평균 이하입니다!")

# sum = 0
# count = 1
# while count <= 5:
#     sum = sum + count
#     count = count + 1
#
# print('총합은', sum)


# 5장 if 연습문제
# tp = 0
# choices = ['a', 'b', 'c']
# for choice in choices:
#     if choice == 'a':
#         tp = tp + 8000
#     elif choice == 'b':
#         tp = tp + 4500
#     elif choice == 'c':
#         tp = tp + 6000
#
# print(tp)

# odd_nums = []
# for num in range(10):
#     if num%2 == 1 :
#         odd_nums.append(num)
#
# print(odd_nums)
#
# cs = ['c1', 'c2', 'c3']
# print(cs)
#
# for c in cs:
#     if c == 'c1':
#         print('안녕')
#     elif c == 'c2':
#         print('반가워')

# year = 2600
# if year % 400 == 0:
#     print(year, '년은 윤년입니다.')
# elif year % 4 == 0 and year % 100 != 0:
#     print(year, '년은 윤년입니다.')
# else:
#     print(year, '년은 윤년이 아닙니다.')

# password = ''
# count = 0
# while password != 'python':
#     password = input('암호:')
#     count += 1
#     if count == 5:
#         print('5회 이상 암호를 틀리셨습니다')
#         break

# price = 0
#
# while price>=0:
#     price = int(input('가격 입력하라'))
#     if price > 10000:
#         print('비쌈')
#     elif price > 5000:
#         print('괜찮음')
#     elif price > 0:
#         print('싸다')

# 숫자 맞추기 게임
#
# import random
#
# x=random.randint(1,20)
#
# while True:
#     num = int(input('수를 입력하라'))
#
#     if x==num:
#         print('정답입니다.')
#         break
#     elif x>num:
#         print('좀 더 큽니다')
#     else:
#         print('좀 작습니다')

# a = {'성별': '여', '나이': 13, '혈액형': 'AB', '전화번호': '02030230'}
# # a['성별'] = '여'
# # a['나이'] = 13
# # a['혈액형'] = 'AB'
# del a['전화번호']
# print(a)

# def add(n1, n2):
#     sum = 1
#     for i in range(n1, n2+1):
#         sum = sum * i
#     return sum
# print(add(3,5))

# def concat(str1, str2):
#     return str1 + str2
#
# print(concat("ef", "eee"))

# def cards(name, num):
#     for i in num:
#         print(name, i , ' 유죄!')
#
# cards('하트', 4)

# import random
#
# a = random.randint(1,6)
# print(a*10)

# score = int(input('점수를 입력하세요'))
# if score >= 90 :
#     print('A')
# elif score< 60:
#     print('c')
# else:
#     print('B')

# i=0
# sum = 0
# while True:
#     i+= 1
#     if i == 10:
#         break
#     elif i % 3 != 0:
#         sum += i
# print(sum)

# a = int(input('정수를 입력하세요.'))
# alist = []
# while a != 0:
#     alist.append(a % 2)
#     a = a // 2
#
# alist.reverse()
#
# print(alist)

def repeat(num=None):
    for i in range(num):
        num = int(input('숫자 입력'))

    print(num)