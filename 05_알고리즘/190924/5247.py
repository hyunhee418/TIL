import sys
sys.stdin = open('5247.txt', 'r')

def func(k, re):
    global M, min_re
    if k < M-N:
        if re == M:
            if min_re > k:
                min_re = k
        else:
            if k < min_re and re < M:
                func(k + 1, re * 2)
                func(k + 1, re + 1)
            if k < min_re and re > M:
                if re - 10 > 0:
                    func(k + 1, re - 10)
                if re - 1 > 0:
                    func(k + 1, re - 1)
T = int(input())
for tc in range(1, 1+3):
    print('#%d' %(tc),end=' ')
    min_re = 100000000
    N, M = map(int, input().split())
    func(0, N)
    print(min_re)