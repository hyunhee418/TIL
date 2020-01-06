import sys
sys.stdin =open('input.txt', 'r')

def perm(k):
    global M, N, result, idx
    t = t1
    if k == M:
        li = [0]*k
        for h in range(k):
            li[h] = t[h]
        if sorted(li) not in result:
            result[idx] = li
            idx += 1
            print(' '.join(map(str, li)))
    else:
        for i in range(N):
            t[k] = l[i]
            perm(k+1)
N, M = map(int, input().split())
idx = 0
result = [0]*(N**M)
l = [i for i in range(1, 1+N)]
t1 = [0]*N
perm(0)