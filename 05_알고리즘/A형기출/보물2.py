import sys
sys.stdin = open('test1.txt', 'r')

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


N, M = map(int, input().split())
arr = [[i for i in input()] for _ in range(N)]
L = []
li_L = []
result = 0
for idx in range(N):
    for j in range(M):
        queue = []
        queue.append((idx, j))
        flag = 0
        visited = [[0] * M for _ in range(N)]
        if arr[idx][j] == 'L':
            while queue != []:
                x, y = queue.pop(0)
                for i in range(4):
                    if 0 <= x+dx[i] < len(arr) and 0 <= y+dy[i] < len(arr[0]):
                        if arr[x+dx[i]][y+dy[i]] == 'L' and visited[x+dx[i]][y+dy[i]] == 0:
                            visited[x+dx[i]][y+dy[i]] = visited[x][y] + 1
                            queue.append([x+dx[i], y+dy[i]])

            for s in range(len(visited)):
                for h in range(len(visited[0])):
                    if visited[s][h] > result:
                        result = visited[s][h]

print(result)