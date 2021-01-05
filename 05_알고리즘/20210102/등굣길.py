dx, dy = [0,0,1,-1], [1,-1, 0,0]
min_l = 10000
def dfs(x, y, a,  m, n, arr, vv):
    global min_l
    if a < min_l:
        for i in range(4):
            if y + dy[i] == n-1 and x + dx[i] == m-1:
                if min_l > a:
                    min_l = a

            if 0<= x+dx[i] < m and 0<= y+dy[i] <n:
                if not arr[y+dy[i]][x+dx[i]] and not vv[y+dy[i]][x+dx[i]]:
                    vv[y+dy[i]][x+dx[i]] =1
                    dfs(x+dx[i], y+dy[i], a+1, m, n, arr, vv)
                    vv[y + dy[i]][x + dx[i]] = 0

def solution(m, n, puddles):
    global min_l
    arr = [[0]*m for _ in range(n)]
    vv = [[0]*m for _ in range(n)]
    for i in range(len(puddles)):
        arr[puddles[i][0]][puddles[i][1]] = 1
    vv[0][0] = 1
    dfs(0,0,0, m,n,arr,vv)
    return min_l


print(solution(4, 3, [[2, 2]]))