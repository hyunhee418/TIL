N = 8
arr = [[0]*N for _ in range(N)]
visited = [[0]*N for _ in range(N)]
result = []
result2 = []
cnt = 0
dx, dy = [0, 1, -1, 0, 1, -1, -1 ,1], [1, 0, 0, -1, 1, -1, 1, -1]
def NQueen(x, y, k):
    global N, cnt
    result.append([x, y])
    visited[x][y] = 1
    for i in range(8):
        s = 0
        idx = 0
        while x + s * dx[idx] < N and y + s * dy[idx] < N:
            arr[x + s * dx[idx]][y + s * dy[idx]] = 1
    if k == N:
        if sorted(result) not in result2:
            result2.append(result)
            cnt += 1
            x2, y2 = result[0]
            NQueen(x2, y2, 0)
    else:
        for x1 in range(N):
            for y1 in range(N):
                if arr[x1][y1] == 0 and not visited[x1][y1]:
                    visited[x1][y1] = 1
                    NQueen(x1, y1, k+1)

for xx in range(N):
    for yy in range(N):
        NQueen(xx, yy, 0)

print(cnt)