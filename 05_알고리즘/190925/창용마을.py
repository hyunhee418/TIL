import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())

def func(x):
    global M, cand
    cand += 1
    visited[x] = 1
    l = 0
    while l < M:
        if ll[l][0] == x and not visited[ll[l][1]]:
            x2 = ll[l][1]
            func(x2)
            l = -1
        elif ll[l][1] == x and not visited[ll[l][0]]:
            x2 = ll[l][0]
            func(x2)
            l = -1
        l += 1

for tc in range(1, 1+T):
    print('#%d' %(tc), end=' ')
    N, M = map(int, input().split())
    visited = [0]*(N+1)
    candidate = [n for n in range(1, 1+N)]
    cnt = 0
    ll = [list(map(int, input().split())) for _ in range(M)]
    for idx in range(N):
        if not visited[candidate[idx]]:
            cand = 0
            visited[candidate[idx]] = 1
            func(candidate[idx])
            if cand:
                cnt += 1
    print(cnt)