import sys
sys.stdin = open('sample_input_5189.txt', 'r')

T = int(input())

def fun1(k, re):
    global N, min_re
    if k == N:
        if re < min_re:
            min_re = re
    else:
        for j in range(k, N):
            l[k], l[j] = l[j], l[k]
            if re < min_re and k+1 < N:
                fun1(k+1, re + arr[l[k]][l[k+1]])
            l[k], l[j] = l[j], l[k]

for tc in range(1, 1+T):
    print('#%d' %(tc), end=' ')
    N = int(input())
    min_re = 1000
    arr = [list(map(int, input().split())) for _ in range(N)]
    l = [i for i in range(1, N)]
    fun1(0, 0)
    print(min_re)