import sys
sys.stdin = open("tc.txt", "r")

T = int(input())
for tc in range(1, T+1):
    print("#%d" %(tc), end=" ")
    a, b = map(int, input().split())
    li = []
    for _ in range(a):
        li.append(str(input()))
    result = [0] * b
    y = -1
    x_1= -1
    while y < len(li) and 0 in result:
        x = 0
        y += 1
        while x < int((len(li[0])) / 2) and 0 in result and y < len(li):
            s = 0
            for i in range(0, int(b / 2 + 1)):
                g = x + b - 1 - i
                if y < len(li) and x + (b - 1) < len(li[0]) and li[y][x] == li[y][x + (b - 1)] and li[y][x + i] == li[y][g]:
                    result[i] = li[y][x + i]
                    result[b - i - 1] = li[y][x + i]
                else:
                    x += 1
    if 0 in result:
        while x_1 < len(li[0]) and 0 in result:
            y_1 = 0
            x_1 += 1
            while y_1 < int((len(li)) / 2) and 0 in result and x_1 < len(li[0]):
                s = 0
                for i in range(0, int(b / 2 + 1)):
                    g = y_1 + b - 1 - i
                    if x_1 < len(li[0]) and y_1 + (b - 1) < len(li) and li[y_1][x_1] == li[y_1 + (b - 1)][x_1] and \
                            li[y_1 + i][x_1] == li[g][x_1]:
                        result[i] = li[y_1 + i][x_1]
                        result[b - i - 1] = li[y_1 + i][x_1]
                    else:
                        y_1 += 1

    print(''.join(result))