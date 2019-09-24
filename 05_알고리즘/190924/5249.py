import sys
sys.stdin = open('5249.txt', 'r')

def func(s):
    global E, value, V
    c = [0]*2*(V+1)
    for i in range(E):
        if E_1[i][0] == s and not t[E_1[i][1]]:
            if value[E_1[i][1]] > E_1[i][2]:
                c[E_1[i][1]] = E_1[i][2]
                value[E_1[i][1]] = E_1[i][2]
                if value[E_1[i][1]] == 10000:
                    for vv in range(len(V_1)):
                        if E_1[i][1] in V_1[vv]:
                            V_1[vv].pop(V_1[vv].index(E_1[i][1]))
                V_1[s].append(E_1[i][1])
        if E_1[i][1] == s and not t[E_1[i][0]]:
            if value[E_1[i][0]] > E_1[i][2]:
                c[E_1[i][0]+V+1] = E_1[i][2]
                value[E_1[i][0]] = E_1[i][2]
                if value[E_1[i][0]] == 10000:
                    for vv in range(len(V_1)):
                        if E_1[i][0] in V_1[vv]:
                            V_1[vv].pop(V_1[vv].index(E_1[i][1]))
                V_1[s].append(E_1[i][0])
    min_v = 10000
    idd = 0
    if sum(c) == 0:
        t[E_1[s][1]] = value[E_1[s][1]]
    for ic in range(len(c)):
        if c[ic]:
            if min_v > c[ic]:
                min_v = c[ic]
                idd = ic
    t[idd % (V+1)] = c[idd]

T = int(input())
for tc in range(1, 1 + T):
    print('#%d' % (tc), end=' ')
    V, E = map(int, input().split())
    V_1 = [[] for _ in range(V+1)]
    E_1 = [list(map(int, input().split())) for _ in range(E)]
    value = [10000] * (V + 1)
    t = [0]*(V+1)
    for v in range(V+1):
        func(v)
    print(t)