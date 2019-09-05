import sys
sys.stdin = open('input_ro.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    d1 = []
    for i in range(N):
        for s in range(N-1, -1, -1):
            print(arr[s][i], end='')
        print(end=' ')

        for j in range(N - 1, -1, -1):
            print(arr[N-i-1][j], end='')
        print(end=' ')

        for h in range(N):
            print(arr[h][N-i-1], end='')
        print()