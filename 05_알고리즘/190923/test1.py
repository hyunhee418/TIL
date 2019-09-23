import sys
sys.stdin = open('test.txt', 'r')

def dfs(x, visited):
    if x not in result:
        result.append(x)
    visited[x] = 1
    for idx in range(8):
        if arr[x][idx] and visited[idx] == 0:
            dfs(idx, visited)


def dfs2(x, visited):
    stack.append(x)
    while stack:
        m = stack.pop()
        if m not in result2:
            result2.append(m)
        if not visited[m]:
            visited[m] = 1
            for g in range(8):
                if arr[m][g] and visited[g] == 0:
                    stack.append(g)



li = list(map(int, input().split()))
arr = [[0]*8 for _ in range(8)]

for i in range(0, len(li)-1, 2):
    arr[li[i]][li[i+1]] = 1
    arr[li[i+1]][li[i]] = 1
visited = [0]*8
visited2 = [0]*8
stack = []
result = []
result2 = []
dfs(1, visited)
dfs2(1, visited2)
print('-'.join(map(str, result)))
print('-'.join(map(str, result2)))

