import sys
sys.stdin = open('2231.txt', 'r')

def check(K):
    global N, re
    K_ele = 0
    n = K
    if K <= N:
        while n // 10:
            K_ele += n % 10
            n //= 10
        K_ele += n
        if K+K_ele == N:
            re = K
            return
        else:
            check(K+1)
N = int(input())
re = 0
check(0)
if re:
    print(re)
else:
    print(0)

