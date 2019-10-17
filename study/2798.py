import sys
sys.stdin = open('2798.txt', 'r')

def game(k):
    global N, min_ab, min_v
    if k == 3:
        if sum(t) <= M:
            if abs(M - sum(t)) <= min_ab:
                min_ab = abs(M - sum(t))
                min_v = sum(t)
    else:
        for i in range(N):
            if visited[i]:
                continue
            t[k] = li[i]
            visited[i] = 1
            game(k+1)
            visited[i] = 0

N, M = map(int, input().split())
li = list(map(int, input().split()))
min_ab = 300000
t = [0]*3
min_v = 300,000
visited = [0]*N
game(0)
print(min_v)

# 29056KB/ 704 ms