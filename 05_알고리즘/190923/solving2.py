import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def check(s, visited, k):
    if k >= 3:
        return
    else:
        i = 0
        while i < N+1:
            if arr[s][i] and visited[s][i] == 0:
                print(i)
                visited[s][i] = 1
                visited[i][s] = 1
                check(i, visited, k+1)
                i=-1
            i += 1

for tc in range(1, 1+T):
    print('#%d' %(tc), end= ' ')
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        arr[x][y] = 1
        arr[y][x] = 1
    visited = [[0]*(N+1) for _ in range(N+1)]
    check(1, visited, 0)
    cnt = 0
    result = []
    print(visited)
    for i in range(N+1):
        for j in range(N+1):
            if visited[i][j] == 1:
                if j not in result:
                    result.append(j)
    print(result)
    if result:
        print(len(result)-1)
    else:
        print(0)