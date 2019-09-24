import sys
sys.stdin = open('5249.txt', 'r')


T = int(input())
for tc in range(1, 1 + T):
    print('#%d' % (tc), end=' ')
    V, E = map(int, input().split())
    E_1 = [list(map(int, input().split())) for _ in range(E)]
    arr = [[0]*(V+1) for i in range(V+1)]
    r = [0]*(V+1)
    for e in E_1:
        arr[e[0]][e[1]] = e[2]
        arr[e[1]][e[0]] = e[2]
    for v in range(V+1):
        min_re = 10000
        idd = 0
        for i in range(V+1):
            if arr[v][i]:
                if arr[v][i] < min_re:
                    min_re = arr[v][i]
                    idd = i
        r[v] = min_re
        arr[idd][v] = 0
        arr[v][idd] = 0
    print(sum(r)-max(r))