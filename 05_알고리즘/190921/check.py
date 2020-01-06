


def perm_r_4(k):
    if k == 3:
        print(t[0], t[1], t[2])
    else:
        for i in range(N):
            if visited[i]: continue
            t[k] = arr[i]
            visited[i] = 1
            perm_r_4(k + 1)
            visited[i] = 0
N = 4
t = [0]*N
arr =[i for i in range(N)]
visited = [0] * N
perm_r_4(0)
