import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
cnt = 0
dx, dy = [0, 1, 0, -1, 1, -1, -1, 1], [1, 0, -1, 0, 1, -1, 1, -1]
def func(x, y, k, arr, result):
    global N, cnt
    if len(result) <= N:
        result.append([x, y])
        if k == N-1 and len(result) == N and sorted(result) not in result2:
            cnt += 1
            arr = [[0] * N for _ in range(N)]
            result2.append(result)
            func(x1, y1, k, arr, [])
        else:
            for xy in range(8):
                s = 0
                while 0<= x+s*dx[xy] < N and 0<= y+s*dy[xy] < N:
                    arr[x+s * dx[xy]][y+s * dy[xy]] = 1
                    s += 1
            for i in range(N):
                for j in range(N):
                    for idx in range(8):
                        if 0 <= i + dx[idx] < N and 0 <= j + dy[idx] < N:
                            if arr[i + dx[idx]][j + dy[idx]] == 0 and (i+dx[idx], j+dy[idx]) not in result:
                                func(i + dx[idx], j + dy[idx], k+1, arr, result)

result2 = []
for x1 in range(N):
    for y1 in range(N):
        arr = [[0] * N for _ in range(N)]
        func(x1, y1, 0, arr, [])
print(cnt)
print(result2)