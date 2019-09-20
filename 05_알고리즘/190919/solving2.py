import sys
sys.stdin = open('input.txt', 'r')

def powerset(k, re):
    global min_re
    if k == N:
        if re < min_re and re >= M:
            min_re = re
    else:
        re1 = re + li[k]
        if re1 < min_re:
            powerset(k + 1, re + li[k])
        powerset(k + 1, re1-li[k])

for tc in range(1, 1+int(input())):
    print('#%d' %(tc), end=' ')
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    min_re = 200000
    powerset(0, 0)
    print(min_re - M)