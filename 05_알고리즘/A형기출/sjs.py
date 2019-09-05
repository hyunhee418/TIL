import sys
sys.stdin = open('test1.txt', 'r')

N, M = map(int, input().split())
arr = [[i for i in input()] for _ in range(N)]
L = []
li_L = []
result = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            L.append([i, j])
def func(li):
    k = L.index(li)
    if  k == 2:
        if li_L not in [L[0], L[1]] and li_L not in [L[1], L[0]]:
            li_L.append([L[0], L[1]])
    else:
        for s in range(k, len(L)):
            L[k], L[s] = L[s], L[k]
            func(L[k+1])
            L[k], L[s] = L[s], L[k]

func(L[0])
print(li_L)