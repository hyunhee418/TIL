import sys
sys.stdin = open('incr.txt', 'r')

from collections import deque

def mono(a):
    i = 0
    while  (a // 10**(i+1)) % 10 != 0:
        if (a // 10**(i)) % 10 < (a // 10**(i+1)) % 10:
            return False
        i += 1
    return True

T = int(input())
for tc in range(1, T+1):
    print('#%d' %tc, end=' ')
    N = int(input())
    li = list(map(int, input().split()))
    value = 0
    for i in range(1<<len(li)):
        l = deque([])
        for j in range(len(li)):
            if i & (1<<j):
                l.append(j)
        if len(l) == 2 and l[0] != l[1] and value < li[l[0]] * li[l[1]] and mono(li[l[0]] * li[l[1]]):
                value = li[l[0]] * li[l[1]]

    if value:
        print(value)
    else:
        print(-1)

