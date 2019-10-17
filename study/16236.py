import sys
sys.stdin = open('16236.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
flag = 0
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
sh = 2
cnt = 0

def isZero(li):
    for xx in range(len(li)):
        if not li[xx]:
            return True
    return False

def check(arr, sh):
    for xx in range(N):
        for yy in range(N):
            if arr[xx][yy] and arr[xx][yy] < sh:
                return True
    return False

# 시작점 찾기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            flag = 1
            break
    if flag:
        break

# while check(arr, sh):
#     can = []
#     min_v = 50
#     for x in range(N):
#         for y in range(N):
#             if arr[x][y] != 0 and arr[x][y] < sh:
#                 can.append([abs(i-x)+abs(j-y), x, y])
#     can.sort()
#
#     j, i, min_v = candida[0]
#
#     cnt += 1
#     if cnt == sh:
#         cnt = 0
#         sh += 1
#     result += min_v
#     arr[i][j] = 0

queue = [(i, j)]
visited = [[0]*N for _ in range(N)]
visited[i][j] = 1
cnt = 0
f = 0

def check(arr, sh):
    for xx in range(N):
        for yy in range(N):
            if arr[xx][yy] and arr[xx][yy] < sh:
                return True
    return False

while check(arr, sh):
    can = []
    for x in range(N):
        for y in range(N):
            if arr[x][y] != 0 and arr[x][y] < sh:
                can.append([x, y])
    v = [0]*len(can)
    while isZero(v) and queue:
        x, y = queue.pop(0)
        for idx in range(4):
            xm = x + dx[idx]
            ym = y + dy[idx]
            if 0 <= xm < N and 0 <= ym < N:
                if (arr[xm][ym] == 0 or arr[xm][ym] == sh or arr[xm][ym] == 9) and not visited[xm][ym]:
                    visited[xm][ym] = visited[x][y] + 1
                    queue.append((xm, ym))
                elif [xm, ym] in can and not visited[xm][ym]:
                    visited[xm][ym] = visited[x][y] + 1
                    v[can.index([xm, ym])] = [visited[xm][ym], xm, ym]
    v.sort()
    min_v, i, j  = v[0]
    result += min_v
    cnt += 1
    arr[i][j] = 0
    queue = [(i, j)]
    if cnt == sh:
        sh += 1
        cnt = 0
    visited = [[0]*N for _ in range(N)]
if f:
    print(v-1)
else:
    print(0)
