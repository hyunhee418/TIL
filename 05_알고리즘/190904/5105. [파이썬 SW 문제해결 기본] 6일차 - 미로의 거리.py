import sys
sys.stdin = open('sample_input (3).txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for tc in range(1, 1+int(input())):
    print('#%d' %(tc), end=' ')
    N = int(input())
    arr = [[int(i) for i in input()] for _ in range(N)]
    flag = 0
    q = []
    result = []
    visited = [[0]*N for _ in range(N)]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 2:
                q.append((i, j))
                flag = 1
        if flag:
            break
    while q != []:
        x, y = q.pop(0)
        for i in range(4):
            if 0 <= x + dx[i] < len(arr) and 0 <= y + dy[i] < len(arr[0]):
                if arr[x + dx[i]][y + dy[i]] == 0:
                    q.append((x+dx[i], y+dy[i]))
                    arr[x][y] = 1
                    visited[x + dx[i]][y + dy[i]] = visited[x][y] + 1
                elif arr[x + dx[i]][y + dy[i]] == 3:
                    result.append(visited[x][y])

    if not result:
        print(0)
    else:
        print(max(result))