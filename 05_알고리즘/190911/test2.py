import sys
sys.stdin = open('test.txt', 'r')


li = [int(i) for i in input()]

result = [0]*(len(li)//7)
for i in range(0, len(li), 7):
    sum_re = 0
    for j in range(7):
        if li[i+j]:
            sum_re += 2**(6-j)

    result[i//7] = sum_re

print(result)