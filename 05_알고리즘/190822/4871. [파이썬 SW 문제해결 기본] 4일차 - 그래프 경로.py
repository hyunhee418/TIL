import sys
sys.stdin = open("sample_input_4871.txt", "r")

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    li_input = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    li = [[0 for _ in range(V)] for _ in range(V)]
    for i in range(len(li_input)):
        li[li_input[i][0]-1][li_input[i][1]-1]  = 1

    y = S-1
    visited = [0]*V
    visited[y] = 1
    stack = [1, y]
    x = 0
    while visited[G-1] != 1 and stack != []:
        for x in range(V):
            if li[y][x] == 1 and visited[x] == 0:
                stack.append(x)
                visited[x] = 1
                y = x

        else:
            y = stack.pop()


    if visited[G-1] == 1:
        print(1)
    else:
        print(0)