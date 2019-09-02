import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    print('#%d' %tc, end=' ')
    N = int(input())
    li = [list(map(int, input().split())) for n in range(N)]
    P = int(input())
    stop = [int(input()) for p in range(P)]
    visited = [0] * len(stop)
    for i in range(len(li)):
        for j in range(li[i][0], li[i][1]+1):
            for s in range(len(stop)):
                if j == stop[s]:
                    visited[s] += 1

    print(' '.join(map(str, visited)))