import sys
sys.stdin = open("input (1).txt", "r")

for tc in range(10):
    T = int(input())
    li = []
    top_li = []
    max_row = 0
    max_i = 0
    re_1 = 0
    re_2 = 0
    for _ in range(100):
        li_1 = list(map(int, input().split()))
        li.append(li_1)

    for row in range(len(li)):
        sum_re = 0
        for i in range(len(li[0])):
            sum_re += li[row][i]
        if sum_re > max_row:
            max_row = sum_re

    for i in range(len(li[0])):
        sum_re = 0
        for row in range(len(li)):
            sum_re += li[row][i]
        if sum_re > max_i:
            max_i = sum_re

    if max_i > max_row:
        max_row = max_i

    for row in range(len(li)):
        for i in range(len(li[0])):
            if i == row:
                re_1 += li[i][row]

    if re_1 > max_row:
        max_row= re_1

    for row in range(len(li)):
        for i in range(len(li[0])):
            if row == len(li[0])-i:
                re_2 += li[i][row]

    if re_2 > max_row:
        max_row = re_2

    print("#%d %d" %(tc, max_row))



    # for _ in range(10):
    # tc = int(input())
    # 