import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(x, depth):
    global result, G
    visited[x] = 1
    if x == G:
        s.append(True)
        print(depth)
        for i in range(len(visited)):
            visited[i] = 1
    if arr[x]:
        try:
            for i in range(len(arr[x])):
                if visited[arr[x][i]] == 0:
                    dfs(arr[x][i], depth+1)
                    visited[x] = 0
        except IndexError:
            pass

T = int(input())
for tc in range(1, 1+T):
    print('#%d' %(tc), end=' ')
    V, E = map(int, input().split())
    input_li = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    result = []
    s = []
    visited = [0]*(V+1)
    for i in range(len(input_li)):
        arr[input_li[i][0]].append(input_li[i][1])
        arr[input_li[i][1]].append(input_li[i][0])
    dfs(S , 0)
    if s:
        pass
    else:
        print(0)

