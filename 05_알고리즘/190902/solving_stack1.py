import sys
sys.stdin = open('input (1).txt', 'r')


def dfs(x):
    if x not in result and x != 0:
        result.append(x)

    if arr[x] and visited[x] == 0:
        for i in range(len(arr[x])):
            try:
                if visited[arr[x][i]] == 0 and point_li[arr[x][i]] > 1:
                    point_li[arr[x][i]] -= 1
                elif visited[arr[x][i]] == 0 and point_li[arr[x][i]] <= 1:
                    visited[x] = 1
                    dfs(arr[x][i])
            except IndexError:
                pass

for tc in range(1, 11):
    print('#%d' %tc, end=' ')
    V, E = map(int, input().split())
    li = list(map(int, input().split()))
    arr = [[] for _ in range(V+1)]
    check_li = []
    visited = [0]*(V+1)
    result = []
    point_li = [0]*(V+1)
    for s in range(1, len(li), 2):
        check_li.append(li[s])
        point_li[li[s]] += 1
    for j in range(0, len(li), 2):
        arr[li[j]].append(li[j+1])
        if li[j] not in check_li and li[j] not in arr[0]:
            arr[0].append(li[j])

    dfs(0)
    for num in range(1, 1+V):
        if num not in result:
            result.append(num)

    print(' '.join(map(str, result)))
