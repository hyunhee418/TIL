import sys
sys.stdin = open('sample_input_A2.txt', 'r')

T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def sum_h(li):
    sum_h = 0
    for i in range(li):
        for j in range(li[0]):
            sum_h += li[i][j]
    return sum_h

for tc in range(1):
    print('#%d' %(tc), end= ' ')
    N = int(input())
    li_input = [list(map(int, input().split())) for _ in range(N)]
    li = [[0]* 2000 for _ in range(2000)]
    s = 0
    result = []

    for n in range(N):
        li[li_input[n][0] + 1000][li_input[n][1] + 1000] = [li_input[n][3], li_input[n][2]]

    while sum_h(li) != 0:
        s += 1
        for y in range(li):
            for x in range(li[0]):
                if li[x + s * dx[li[y][x][1]][y + s * dy[li[y][x][1]] != 0:
                    print(li[x][y])

                #     result.append(li[y + s * dy[li[y][x][1]]][x + s * dx[li[y][x][1]]][0] + li[x][y][0])
                #     li[y + s * dy[li[y][x][1]]][x + s * dx[li[y][x][1]]] = 0
                #     li[x][y] = 0
                # else:
                #     li[y + s * dy[li[y][x][1]]][x + s * dx[li[y][x][1]]] = li[x][y]
                #     y = y + s * dy[li[y][x][1]]
                #     x = x + s * dx[li[y][x][1]]
                #     li[x][y] = 0