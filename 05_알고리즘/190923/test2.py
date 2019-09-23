import sys
sys.stdin = open('test.txt', 'r')

def bfs():
    while queue:
        m = queue.pop(0)
        if m not in result:
            result.append(m)
        visited[m] = 1
        for j in range(8):
            if arr[m][j] and not visited[j]:
                queue.append(j)

li = list(map(int, input().split()))
arr = [[0]*8 for _ in range(8)]

for i in range(0, len(li)-1, 2):
    arr[li[i]][li[i+1]] = 1
    arr[li[i+1]][li[i]] = 1

visited = [0]*8
result = []
queue = [1]
bfs()
print('-'.join(map(str, result)))