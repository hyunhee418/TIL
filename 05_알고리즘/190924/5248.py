import sys
sys.stdin = open('5248.txt', 'r')


def dfs(x):
    for i in range(M+1):
        if arr[x][i] and not visited[i]:
            visited[i] = 1
            ele.append(i)
            dfs(i)



T = int(input())
for tc in range(1, 1+T):
    print('#%d' %(tc), end=' ')
    M, N = map(int, input().split())
    nums = [n for n in range(1, M+1)]
    arr = [[0]*(M+1) for _ in range(M+1)]
    r = []
    li = list(map(int, input().split()))
    for i in range(0, len(li), 2):
        arr[li[i]][li[i+1]] = 1
        arr[li[i+1]][li[i]] = 1
    visited = [0]*(M+1)
    for num in nums:
        if not visited[num]:
            ele = [num]
            visited[num] = 1
            dfs(num)
            if ele not in r:
                r.append(ele)
    print(len(r))