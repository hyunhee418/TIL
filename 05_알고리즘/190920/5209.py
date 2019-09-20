import sys
sys.stdin = open('sample_input_5209.txt', 'r')

def perm(k, re):
    global N, min_re
    if k == N:
        if re < min_re:
            min_re = re
    else:
        for i in range(k, N):
            l[k], l[i] = l[i], l[k]
            if re < min_re:
                perm(k+1, re+arr[k][l[k]])
            l[k], l[i] = l[i], l[k]

for tc in range(1, 1+int(input())):
    print('#%d' %(tc), end=' ')
    N = int(input())
    min_re = 1485
    arr = [list(map(int, input().split())) for _ in range(N)]
    l = [i for i in range(N)]
    perm(0, 0)
    print(min_re)