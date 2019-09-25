import sys
sys.stdin = open('input (1).txt', 'r')

def check(aa, k):
    aa1 = aa[:]
    global max_re
    if k == 2:
        aa1[t[0]], aa1[t[1]] = aa1[t[1]], aa1[t[0]]
        r.append(aa1)
    else:
        for i in range(len(a)):
            if visited[i]:
                continue
            t[k] = l[i]
            visited[i] = 1
            check(aa, k+1)
            visited[i] = 0

T = int(input())
for tc in range(1, 1+T):
    a, b = map(str, input().split())
    max_re = 0
    l = [num for num in range(len(a))]
    visited = [0]*(len(a))
    t = [0, 0]
    r = []
    aa = [ii for ii in a]
    check(aa, 0)
    for id in range(len(r)):
        if int(''.join(r[id])) > max_re:
            max_re = int(''.join(r[id]))
    print(max_re)