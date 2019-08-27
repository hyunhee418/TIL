li_input = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
li = [[0]*8 for _ in range(8)]
for i in range(0, len(li_input), 2):
    li[li_input[i]][li_input[i+1]] = 1
    li[li_input[i+1]][li_input[i]] = 1

v = 1
result = []
def bfs(li, v):
    visited = [0] * 8
    q = []
    q.append(v)
    while q:
        t = q.pop(0)
        if not visited[t]:
            visited[t] = 1
            result.append(t)

        for i in range(len(li[t])):
            if li[t][i] == 1 and visited[i] == 0:
                q. append(i)


bfs(li, 1)
print('-'.join(map(str, result)))