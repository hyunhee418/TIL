import sys
sys.stdin = open('input.txt', 'r')


def powerset(k, re, N):
    global min_re, M
    if k == N:
        if re > M:
            if re < min_re:
                min_re = re
    else:
        for i in range(len(li)):
            if visited[i]:
                continue
            visited[i] = 1
            if re < min_re:
                powerset(k+1, re+li[i], N)
            visited[i] = 0

for tc in range(1, 1+int(input())):
    print('#%d' %(tc), end=' ')
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    visited = [0]*(len(li))
    min_re = 200000
    for N in range(1, len(li)+1):
        t = [0]* N
        powerset(0, 0, N)
    print(min_re - M)