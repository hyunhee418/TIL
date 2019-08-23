import sys
sys.stdin = open("02.txt", "r")

T = int(input())
for tc in range(1, T+1):
    print("#%d" %(tc), end =" ")
    N, M, K = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]
    max_h = 0
    for j in range(N - K + 1):
        for i in range(M - K + 1):
            sum_h = 0
            for x in range(K):
                sum_h += li[j][i+x]

                sum_h += li[j+x][i]
                sum_h += li[j+K-1][i+x]
                sum_h += li[j+x][i+K-1]
            sum_h -= (li[j][i] + li[j+K-1][i] + li[j+K-1][i+ K -1] +li[j][i+K-1])
            if sum_h > max_h:
                max_h = sum_h

    print(max_h)