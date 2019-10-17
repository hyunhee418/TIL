import sys, copy
sys.stdin = open('1018.txt', 'r')

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def check(arr, xx, yy):
    global cnt, N, M
    l = copy.deepcopy(arr)
    l[xx][yy] = 'W'
    for x in range(xx, xx+8):
        for y in range(yy, yy+8):
            for idx in range(4):
                if x == xx and idx == 2:
                    pass
                elif y == yy and idx == 0:
                    pass
                elif x == xx+7 and idx == 3:
                    pass
                elif y == yy+7 and idx == 1:
                    pass
                else:
                    if 0 <= x + dx[idx] < N and 0 <= y + dy[idx] < M:
                        if l[x][y] == l[x + dx[idx]][y + dy[idx]]:
                            cnt += 1
                            if l[x + dx[idx]][y + dy[idx]] == 'B':
                                l[x + dx[idx]][y + dy[idx]] = 'W'
                            else:
                                l[x + dx[idx]][y + dy[idx]] = 'B'
    l = copy.deepcopy(arr)
    l[xx][yy] = 'B'
    cnt2 = 0
    for x in range(xx, xx+8):
        for y in range(yy, yy+8):
            for idx in range(4):
                if x == xx and idx == 2:
                    pass
                elif y == yy and idx == 0:
                    pass
                elif x == xx+7 and idx == 3:
                    pass
                elif y == yy+7 and idx == 1:
                    pass
                else:
                    if 0 <= x + dx[idx] < N and 0 <= y + dy[idx] < M:
                        if l[x][y] == l[x + dx[idx]][y + dy[idx]]:
                            cnt2 += 1
                            if l[x + dx[idx]][y + dy[idx]] == 'B':
                                l[x + dx[idx]][y + dy[idx]] = 'W'
                            else:
                                l[x + dx[idx]][y + dy[idx]] = 'B'
    if cnt2 < cnt:
        cnt = cnt2
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
min_c = 64
for xx in range(0, N-8+1):
    for yy in range(0, M-8+1):
        cnt = 0
        check(arr, xx, yy)
        if cnt < min_c:
            min_c = cnt
print(min_c)