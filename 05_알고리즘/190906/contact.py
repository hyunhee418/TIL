import sys
sys.stdin = open('input_contact.txt', 'r')

for tc in range(10):
    print('#%d' %(tc), end=' ')
    N, S = map(int, input().split())
    li = list(map(int, input().split()))
    queue = []
    queue.append(S)
    visited = [0] * (max(li)+2)
    idx_li = []
    visited[S] = 1
    while queue:
        x = queue.pop(0)
        for i in range(0, len(li)-1, 2):
            if li[i] == x and visited[li[i+1]] == 0:
                visited[li[i+1]] = visited[x] + 1
                queue.append(li[i+1])
    a = max(visited)
    while max(visited) == a:
        b = visited.index(max(visited))
        idx_li.append(b)
        visited[b] -= 1
    print(max(idx_li))