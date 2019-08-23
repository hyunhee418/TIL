for tc in range(1, TC+1):
    N = int(input())

    mat = [0]*N
    for i in range(N):
        mat[i] = list(map(int, input().split()))


    dx = [0, 1, 0, -1, -1, 1, -1, 1]
    dy = [1, 0, -1, 0, -1, 1, 1, -1]

    def dfs(x, y):
        if not (0 <= x < N and 0 <= y < N):
            return
        if not mat[x][y]:
            return
        mat[x][y] = 0

        for i in range(8):
            dfs(x + dx[i], y + dy[i])


    ans = 0

    for i in range(N):
        for j in range(N):
            if mat[i][j]:
                dfs(i, j)
                ans += 1
    print("#%d" % tc, ans)

