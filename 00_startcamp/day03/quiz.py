# # name = input('What\'s your name?:')  # 입력을 받는 함수
# # print('hi, ' + name)

# words = input('입력고고: ')
# print(type(words))
# print(words[0], words[-1])
# # numbers=[1, 2, 3, 4, 5]

# import random

# length = random.choice(range(1,100))
# numbers = list(range(length))  # [0, 1, 2, ... length-1]
# print(numbers[0], numbers[-1])  # numbers[length-1]

# # 언제나 list[-1]은 마지막 value

# n을 입력받고, 1부터 n까지 출력하라

# n = input('자연수를 입력해주세요.: ')
# # print(list(range(1,int(n) + 1)))
# n = int(n)
# for i in range(n):
#     print(i + 1, end=' ')  # end=' ' 배열 끝에 띄어쓰기를 넣겠다.


# n = input('자연수를 입력해주세요: ')
# n = int(n)  # str => list(str) / str => int(str)
# numbers = list(range(1,int(n) + 1))
# print(type(numbers[0]))
# print(numbers[0], numbers[-1])

# number = int(input('숫자를 입력하세요: '))

# if number % 2 == 0:
#     print("짝")
# else:
#     print("홀")

#fizz buzz => 3배수 fizz / 5배수 buzz / 15배수 fizzbuzz
# for i in range(1,number+1):
#     if i % 15 == 0:
#         print('fizzbuzz', end = ' ')
#     elif i % 5 == 0:
#         print('buzz', end = ' ')
#     elif i % 3 == 0:
#         print('fizz', end = ' ')
#     else:
#         print(i, end = ' ')

