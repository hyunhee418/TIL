import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def move(x, y, re, k):
    global min_re, N
    if k == 2*N-1:
        if re < min_re:
            min_re = re
    for i in range(2):
        if 0 <= x < N and 0 <= y < N:
            re += arr[x][y]
            if re < min_re:
                move(x + dx[i], y + dy[i], re, k+1)
            re -= arr[x][y]


dx, dy = [0, 1], [1, 0]

for tc in range(1, 1+T):
    print('#%d' %(tc), end=' ')
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_re = 650
    move(0, 0, 0, 0)
    print(min_re)
