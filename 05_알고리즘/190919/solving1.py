import sys
sys.stdin = open('input.txt', 'r')



for tc in range(1, 1 + int(input())):
    print('#%d' % (tc), end=' ')
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    min_re = 200000
    r = [[]]
    for i in li:
        ele = [x + [i] for x in r]
        r += ele
    for i in r:
        a = sum(i)
        if a >= M:
            if a < min_re:
                min_re = a
    print(min_re - M)