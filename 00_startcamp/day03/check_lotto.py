my = [1, 2, 3, 4, 5, 6]

real = [1, 2, 3, 4, 5, 7]
bonus = [6]

# my와 real 의 숫자가 모두 같으면 1등
# my와 real 이 5개가 같고 나머지 하나가 bonus 면 2등
# my와 real 이 5개가 같으면 3등
# 4개가 같으면 4등
# 3개가 같으면 5등
# 나머지는 꽝

# 내 방식
rest = list(set(my) - set(real))
rest2 = list(set(rest) - set(bonus))

if len(rest) == 0:
    print('1등!!!')
elif len(list(rest2)) == 0:
    print('2등!!!')
elif len(rest) == 1:
    print('3등!!!')    
elif len(rest) == 2:
    print('4등!!!')
elif len(rest) == 3:
    print('5등!!!')
else:
    print('꽝!!!')

# 1번 방식
count = 0
is_bonus = False  # i == bonus가 되야 is_bonus가 등장하기 때문에 만일 같지 않다면 주석처리됨. 따라서, elif에서 5개 같을 때 갑자기 등장. 그러므로 is_bonus가 false라고 정의해두면 가능.
for i in my:
#     if i == bonus:
        # is_bonus = True
if bonus in my:
       is_bonus = True

    for j in real:
        if i == j:
        # count = count + 1
            count += 1

# 2번 방식
# [1, 2, 3]->list / {1, 2, 3}->set / (1, 2, 3)->tuple / {'a: 'A'}->dic
match = set(my).intersection(set(real))
count = len(match)

if count == 6:
    result = '1등'
elif count == 5:
    if is_bonus:
# if bonus in my:  이를 쓰면 굳이 위에 for i in my ~ bonus까지 지워도 된다. (컴퓨터 일 덜 시키는 방법->일이 더 빨라짐.)
        result = '2등'
    else:
        result = '3등'
elif count == 4:
    result = '4등'
elif count == 3:
    result = '5등'
else:
    result = '꽝!'  # 앞으로는 print가 결과가 되지 않음 디버깅용

