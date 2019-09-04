import sys
sys.stdin = open('input (2).txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print('#%d' %(tc), end=' ')
    li = list(map(int, input().split()))
    point_x = 0
    point_y = 0
    num_s = 0
    for N in li:
        check_s = 0
        for i in range(1, N+1):
            if check_s + i >= N:
                break
            check_s += i
        point_x += i - (N - check_s) + 1
        point_y += N - check_s
    for a in range(1, point_y+point_x-1):
        num_s += a
    print(num_s + point_y)
    #
    # for s in range(1, M+1):
    #     if check_s + s >= M:
    #         break
    #     check_s += s
    # point_M_x = s - (M - check_s) + 1
    # point_M_y = M - check_s
    # stair = point_N_x + point_N_y - 1 + point_M_x + point_M_y
    # num_s = 0
    # for a in range(1, stair):
    #     num_s += a
    # print(num_s + point_N_y + point_M_y)