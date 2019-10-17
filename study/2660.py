import sys
sys.stdin = open('2660.txt', 'r')

def bfs(x, visited):
    queue = [x]
    while queue:
        s = queue.pop(0)
        if s:
            for f in range(len(l[s])):
                if not visited[l[s][f]]:
                    visited[l[s][f]] = visited[s] + 1
                    queue.append(l[s][f])
    return visited
N = int(input())
l = [[] for _ in range(N+1)]
user = [num for num in range(1, N+1)]
min_sc = 50
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    else:
        l[b].append(a)
        l[a].append(b)
can = []
for u in range(len(user)):
    visited = [0]*(N+1)
    visited[user[u]] = 1
    re = max(bfs(user[u], visited))
    if re < min_sc:
        min_sc = re
        can = [user[u]]
    elif re == min_sc:
        min_sc = re
        can.append(user[u])
print(min_sc-1, len(can))
for c in can:
    print(c, end=' ')