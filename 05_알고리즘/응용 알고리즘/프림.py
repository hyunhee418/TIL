import sys
sys.stdin = open('sample_input.txt', 'r')

def MST_PRIM(G, s):
    key[s] = 0

    for _ in range(N):
        minidx = -1
        min_v = 1000000
        for i in range(N):
            if not visited[i] and key[i] < min_v:
                min_v = key[i]
                minidx = i
        visited[minidx] = 1
        for v, val in G[minidx]:
            if not visited[v] and val < key[v]:
                key[v] = val
                pi[v] = minidx


for tc in range(1, 1+int(input())):
    print('#%d' %(tc),end=' ')
    V, E = map(int, input().split())
    N = V+1
    li = [list(map(int, input().split())) for _ in range(E)]
    G = [[] for _ in range(V+1)]
    for l in range(len(li)):
        G[li[l][0]].append((li[l][1], li[l][2]))
        G[li[l][1]].append((li[l][0], li[l][2]))
    key = [10000000] * N
    pi = [0] * N
    visited = [0] * N
    MST_PRIM(G, 0)
    print(sum(key))