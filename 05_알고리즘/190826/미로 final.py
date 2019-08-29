dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


for tc in range(1, int(input()) + 1):
    print('#{}'.format(tc), end=' ')
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    stack = [(1000, 1000)]
    f = 0

    for x in range(N):
        for y in range(N):
            if arr[x][y] == 2:
                stack.append((x, y))

    x, y = stack[-1]

    while stack:
        i = 0
        while i < 4:
            y2 = y + dy[i]
            x2 = x + dx[i]
            if N > y2 >= 0 and N > x2 >= 0:
                if arr[x2][y2] == 3:
                    print(1)
                    f = 1
                    break
                elif arr[x2][y2] == 0:
                    arr[x2][y2] = 1
                    stack.append((x2, y2))
                    x = x2
                    y = y2
                    i = -1
            i += 1
        x, y = stack[-1]
        for i in range(4):
            if N > y + dy[i] >= 0 and N > x + dx[i] >= 0:
                if not arr[x + dx[i]][y + dy[i]]:
                    break
            else:
                pass
        else:
            stack.pop()
        if f:
            break
    if f == 0:
        print(0)
