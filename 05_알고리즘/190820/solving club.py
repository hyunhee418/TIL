import sys
sys.stdin = open("input.txt", "r")

for tc in range(10):
    S = int(input())
    N = [list(map(int, input().split())) for _ in range(100)]
    x = 0
    y= 99
    count_1 = 0
    count_2 = 0
    z = 0
    li = []
    while N[y][x] != 2:
       x += 1
    li.append([y, x])
    print(li)

    if x != 0 :
        x_1 = li[z][1]
        y_1 = li[z][0]
        while N[y][x-1] != 1:
            y_1 -= 1
            count_1 += 1
        li.append([y_1, x_1])
        print(li, y_1, x_1, count_1)
        x = x_1 - 1
        while N[y_1][x_1] == 1:
            x_1 -= 1
            count_1 += 1
        li.append([y_1, x_1])
        print(li, y_1, x_1, count_1)

    if x != 99:
        x = li[0][1]
        y = li[0][0]
        while N[y][x + 1] != 1:
            y -= 1
            count_2 += 1
        li.append([y, x])
        print(li, y, x, count_2)
        x = x + 1
        while N[y][x] == 1:
            x += 1
            count_2 += 1
        li.append([y, x])
        print(li, y, x, count_2)


