import sys
sys.stdin = open('input.txt', 'r')



def perm(k):
    global M, N, result
    if k == M:
        li = []
        for h in range(k):
            li.append(l[h])
        if sorted(li) not in result:
            result.append(li)
            print(' '.join(map(str, li)))
    else:
        for j in range(k, N):
            l[k], l[j] = l[j], l[k]
            perm(k+1)
            l[k], l[j] = l[j], l[k]

N, M = map(int, input().split())
result = []
l = [i for i in range(1, 1+N)]
perm(0)