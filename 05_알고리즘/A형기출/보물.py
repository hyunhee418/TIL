N, M = map(int, input().split())
arr = [[i for i in input()] for _ in range(N)]
L = []
# li_L = []
result = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            L.append([i, j])


def func(li):
    global result
    k = L.index(li)
    if k == 2:
        # if li_L not in [L[0], L[1]] and li_L not in [L[1], L[0]]:
        # li_L.append([L[0], L[1]])
        # for i in range(len(li_L)):
        S = L[0]
        G = L[1]
        queue = []
        queue.append(S)
        x, y = 0, 0
        flag = 0
        visited = [[0] * M for _ in range(N)]
        visited[S[0]][S[1]] = 0
        while queue != [] and (x != G[0] or y != G[1]):
            l = queue.pop(0)
            x, y = l[0], l[1]
            for i in range(4):
                x2 = x + dx[i]
                y2 = y + dy[i]
                if 0 <= x + dx[i] < len(arr) and 0 <= y + dy[i] < len(arr[0]):
                    if arr[x + dx[i]][y + dy[i]] == 'L' and visited[x + dx[i]][y + dy[i]] == 0:
                        visited[x + dx[i]][y + dy[i]] = visited[x][y] + 1
                        queue.append([x + dx[i], y + dy[i]])
                        if x + dx[i] == G[0] and y + dy[i] == G[1]:
                            flag = 1
                            break
                if flag:
                    break
            if flag and visited[x][y] > result:
                result = visited[x][y]
    else:
        for s in range(k, len(L)):
            L[k], L[s] = L[s], L[k]
            func(L[k + 1])
            L[k], L[s] = L[s], L[k]


func(L[0])
#
# for i in range(len(li_L)):
#     S = li_L[i][0]
#     G = li_L[i][1]
#     queue = []
#     queue.append(S)
#     x, y = 0, 0
#     flag = 0
#     visited = [[0]*M for _ in range(N)]
#     visited[S[0]][S[1]] = 1
#     while queue != [] and (x != G[0] or y != G[1]):
#         l = queue.pop(0)
#         x, y = l[0], l[1]
#         for i in range(4):
#             x2 = x + dx[i]
#             y2 = y + dy[i]
#             if 0 <= x+dx[i] < len(arr) and 0 <= y+dy[i] < len(arr[0]):
#                 if arr[x+dx[i]][y+dy[i]] == 'L' and visited[x+dx[i]][y+dy[i]] == 0:
#                     visited[x+dx[i]][y+dy[i]] = visited[x][y] + 1
#                     queue.append([x+dx[i], y+dy[i]])
#                     if x+dx[i] == G[0] and y+dy[i] == G[1]:
#                         flag = 1
#                         break
#         if flag:
#             break
#     if flag:
#         result.append(visited[x][y])

print(result)
# print(max(result))