my = [1, 2, 3, 4, 5, 6]

real = [1, 2, 3, 4, 5, 7]
bonus = [6]

# my와 real 의 숫자가 모두 같으면 1등
# my와 real 이 5개가 같고 나머지 하나가 bonus 면 2등
# my와 real 이 5개가 같으면 3등
# 4개가 같으면 4등
# 3개가 같으면 5등
# 나머지는 꽝

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
