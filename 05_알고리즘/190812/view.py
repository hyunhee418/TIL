import sys
sys.stdin = open("input.txt", "r")


def find(N, H):
    H.insert(-1, 0)
    res = 0
    for i in range(2, N - 2):
        i_max = 255
        nth = -2
        while  nth != 3 and H[i] - H[i + nth] >= 0:
            if H[i] - H[i + nth] <= i_max and H[i] - H[i + nth] != 0:
                i_max = H[i] - H[i + nth]
            nth += 1
        if H[i] - H[i + nth] < 0:
            pass

        elif i_max != 255:
            res += i_max

            print(i, i_max)
            # i_max = 255
        # elif i_max != 255:
        # if H[i] - H[i + nth] < 0:
        #     pass
        # elif i_max != 255:
        #     res += i_max
        # #     i_max = 255
        #         # res += i_max
        #         # i_max = 255

    return res


T = 1
for tc in range(1, T+1):
    N = int(input())
    H = list(map(int, input().split()))

    res = find(N, H)
    print("#%d %d" % (tc, res) )