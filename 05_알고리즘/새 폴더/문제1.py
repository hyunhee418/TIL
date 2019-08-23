import sys
sys.stdin = open("01.txt", "r")

T = int(input())

for tc in range(1, 1+T):
    print("#%d" %(tc), end=" ")
    a, b = map(int, input().split())
    li_input = [list(map(int, input().split())) for _ in range(b)]
    count = 0
    li = [[0 for _ in range(a)] for _ in range(a)]
    for x in range(len(li_input)):
        for i in  range(li_input[x][0]-1, li_input[x][2]):
            for j in range(li_input[x][1]-1, li_input[x][3]):
                li[i][j] = 1

    for y_1 in range(len(li)):
        for x_1 in range(len(li[0])):
            if li[y_1][x_1] == 1:
                count += 1

    print(count)