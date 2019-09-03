import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    print('#%d' %(tc), end=' ')
    V, E = map(int, input().split())
    input_li = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    arr = [[0]*(V+1) for _ in range(V+1)]
    for i in range(len(input_li)):
        arr[input_li[i][0]][input_li[i][1]] = 1
        arr[input_li[i][1]][input_li[i][0]] = 1
    stack = []
    visited = [0] * (V+1)
    stack.append(S)
    visited[S] = 1
    f = 0
    i = S
    while stack:
        x = 0
        while x < len(arr[i]):
            if i == G:
                print(len(stack)-1)
                f = 1
                break
            if arr[i][x] == 1 and visited[x] == 0:
                i = x
                visited[x] = 1
                x = -1
                stack.append(i)
            x += 1
        if f:
            break
        i = stack[-1]
        x = 0
        while x < len(arr[i]):
            if arr[i][x] == 1 and visited[x] == 0:
                break
            x += 1
        else:
            i = stack.pop()

    if f == 0:
        print(len(stack))
