import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())


def check():
    global N, cnt, visited
    while q:
        s = q.pop(0)
        if s == 1:
            visited[s] = 1
        for idx in range(N+1):
            if arr[s][idx] and visited[idx] == 0:
                visited[idx] = visited[s] + 1
                q.append(idx)

for tc in range(1, 1+T):
    print('#%d' %(tc), end= ' ')
    cnt = 0
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        arr[x][y] = 1
        arr[y][x] = 1
    visited = [0]*(N+1)
    q = [1]
    check()
    for i in visited:
        if i < 4 and i != 0:
            cnt += 1
    print(cnt-1)