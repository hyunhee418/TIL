# 인자는 N개 들어옵니다. 모든 인자를 더하는 함수를 구현하시오.
# my_sum()을 만들고, 예시 결과
# my_sum(1, 2, 3) # 6
# 그런데 정수/ 실수 아닌 자료형이 들어오면 '실패'를 리턴하세요.
def my_sum(*args):
    for e in args:
        if type(e) not in (int, float):
            return 'fail'
    return sum(args)

print(my_sum(1, 2.3, 4, 'a'))
print(my_sum(1, 2.3, 4))
print(my_sum(1))
print(my_sum(True))
