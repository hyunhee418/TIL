import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    print('#%d' %(tc), end=' ')
    V, E = map(int, input().split())
    input_li = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    queue = []
    queue.append(S)
    visited = [0]*(V+1)
    x = 0
    visited[S] = 1
    while x != G and queue != []:
        x = queue.pop(0)
        for li in input_li:
            if x in li:
                if visited[li[(li.index(x) + 1) % 2]] == 0:
                    queue.append(li[(li.index(x) + 1) % 2])
                    visited[li[(li.index(x) + 1) % 2]] = visited[x] + 1
    if x == G:
        print(visited[G]-1)
    else:
        print(0)