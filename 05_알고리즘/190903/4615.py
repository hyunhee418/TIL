import sys
sys.stdin = open('4615.txt', 'r')

dx = [0, 0, -1, 1, 1, -1, 1, -1]
dy = [-1, 1, 0, 0, 1, -1, -1, 1]
T = int(input())
for tc in range(1, T+1):
    print('#%d' %(tc), end=' ')
    N, M = map(int, input().split())
    arr = [[0]* N for _ in range(N)]


    arr[N // 2 - 1][N // 2 - 1] = arr[N // 2][N // 2] = 2
    arr[N // 2 - 1][N // 2] = arr[N // 2][N // 2 - 1] = 1

    li = [list(map(int, input().split())) for _ in range(M)]
    for i in range(len(li)):
        for idx in range(8):
            s = 2
            while 0 <= li[i][1]+s*dy[idx]-1 < len(arr) and 0 <= li[i][0]+s*dx[idx]-1 < len(arr[0]):
                if arr[li[i][1]+(s-1)*dy[idx]-1][li[i][0]+(s-1)*dx[idx]-1] == 0 or arr[li[i][1]+(s-1)*dy[idx]-1][li[i][0]+(s-1)*dx[idx]-1] == li[i][2]:
                    break
                elif arr[li[i][1]+s*dy[idx]-1][li[i][0]+s*dx[idx]-1] == li[i][2]:
                    for g in range(s):
                        arr[li[i][1] + g*dy[idx]-1][li[i][0] + g*dx[idx]-1] = li[i][2]
                    break
                s += 1
    sum_b = 0
    sum_w = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                sum_b += 1
            elif arr[i][j] == 2:
                sum_w += 1
    print(sum_b, sum_w)
