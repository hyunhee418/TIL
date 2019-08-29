import sys
from collections import deque

sys.stdin = open('test2.txt', 'r')

arr = deque([deque(map(int, input().split())) for _ in range(10)])
dx = [0, 0, -1, 1, 1, -1, -1, 1]
dy = [ -1, 1, 0, 0, 1, -1, 1, -1]
cnt = 0



for y in range(10):
    for x in range(10):
        if arr[y][x] == 3:
            i = 0
            s = 0

            while i < 8:
                y2 = y + s * dy[i]
                x2 = x + s * dx[i]
                if x+ s* dx[i] < 0 or y+ s* dy[i] < 0 or y+ s* dy[i] >= len(arr) or x+ s* dx[i] >= len(arr[0]):
                    i += 1
                    s = 0

                elif arr[y + s * dy[i]][x+ s * dx[i]] == 1:
                    cnt += 1
                    arr[y + s * dy[i]][x + s * dx[i]] = 0

                elif arr[y+ s * dy[i]][x+ s * dx[i]] == 2:
                    i += 1
                    s = 0
                elif y+ s* dy[i] > len(arr) or x+ s* dx[i] > len(arr[0]):
                    i += 1
                    s = 0
                s += 1

print(cnt)