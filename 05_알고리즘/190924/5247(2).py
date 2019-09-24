import sys
from collections import deque
sys.stdin = open('5247.txt', 'r')

def bfs():
    global M
    while q:
        x = q.popleft()
        if x == M:
            print(l[x]-1)
            break
        else:
            if x+1 <= 1000000:
                if not l[x+1]:
                    q.append(x+1)
                    l[x+1] = l[x] + 1
            if x*2 <= 1000000:
                if not l[x*2]:
                    q.append(x*2)
                    l[x*2] = l[x] + 1
            if x-1 > 1:
                if not l[x-1]:
                    q.append(x-1)
                    l[x-1] = l[x] + 1
            if x-10 > 1:
                if not l[x - 10]:
                    q.append(x-10)
                    l[x-10] = l[x] + 1
for tc in range(1, 1+int(input())):
    print('#%d' %(tc), end=' ')
    N, M = map(int, input().split())
    l = [0]*1000001
    l[N] = 1
    q = deque([N])
    bfs()