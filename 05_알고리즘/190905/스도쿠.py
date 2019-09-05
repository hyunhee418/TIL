import sys
sys.stdin = open('input (6).txt', 'r')

for tc in range(1, int(input())+1):
    print('#%d' %(tc), end=' ')
    li = [list(map(int, input().split())) for _ in range(9)]
    flag = 0
    for i in range(9):
        visited_x = [0] * 10
        visited_y = [0] * 10
        for j in range(9):
            if visited_x[li[i][j]] != 0:
                flag = 1
                break
            else:
                visited_x[li[i][j]] = 1
            if visited_y[li[j][i]] != 0:
                flag = 1
                break
            else:
                visited_y[li[j][i]] = 1
            if i % 3 == 0 and j % 3 == 0:
                visited_3 = [0]*10
                for x in range(3):
                    for y in range(3):
                        if visited_3[li[i+x][j+y]] != 0:
                            flag = 1
                            break
                        else:
                            visited_3[li[i+x][j+y]] = 1

                    if flag:
                        break

            if flag:
                break
        if flag:
            break

    if flag:
        print(0)
    else:
        print(1)