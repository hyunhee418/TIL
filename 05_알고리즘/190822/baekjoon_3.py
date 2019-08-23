import sys
sys.stdin = open("baekjoon_3.txt", "r")

li = [list(map(int, input().split())) for _ in range(5)]
count = 0
stop = 0
for tc in range(5):
    l = list(map(int, input().split()))
    for i in range(5):
        for x in range(5):
            for y in range(5):
                if l[i] == li[x][y]:
                    li[x][y] = 0
                    su = 0
                    su_s = 0
                    su_i = 0
                    su_j = 0
                    for z in range(5):
                        su += li[x][z]
                        su_s += li[z][y]
                        su_i += li[z][z]
                        su_j += li[z][4 - z]
                    if su == 0:
                        stop += 1
                        for z in range(5):
                            li[x][z] = 100
                    if su_s == 0:
                        stop += 1
                        for z in range(5):
                            li[z][y] = 100
                    if su_i == 0:
                        stop += 1
                        for z in range(5):
                            li[z][z] = 100
                    if su_j == 0:
                        stop += 1
                        for z in range(5):
                            li[z][4- z] = 100

                    if stop == 3:
                        print(count)
                        break
                    else:
                        count += 1
