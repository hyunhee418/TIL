import sys
sys.stdin = open('5251.txt', 'r')

def func(k, s):
    global E, value, V
    c = [0]*(V+1)
    if k == E-1:
        return
    else:
        for i in range(k, E):
            if E_1[i][0] == s:
                c[E_1[i][1]] = 1
                if value[E_1[i][1]] > value[s] + E_1[i][2]:
                    value[E_1[i][1]] = value[s] + E_1[i][2]
        else:
            min_re = 10000
            idd = 0
            for ele_c in range(len(c)):
                if c[ele_c]:
                    if value[ele_c] < min_re:
                        min_re = value[ele_c]
                        idd = ele_c
            func(k+1, idd)

T = int(input())
for tc in range(1, 1+T):
    print('#%d' %(tc), end=' ')
    V, E = map(int, input().split())
    E_1 = [list(map(int, input().split())) for _ in range(E)]
    value = [10000]*(V+1)
    value[0] = 0
    func(0, 0)
    print(value[-1])