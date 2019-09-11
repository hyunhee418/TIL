import sys
sys.stdin = open('sample_inpu.txt', 'r')

T = int(input())

for tc in range(1, 1+T):
    print('#%d' %(tc), end=' ')
    N, M, L = map(int, input().split())
    input_li = [list(map(int, input().split())) for _ in range(M)]
    li = [0]*(N+1)
    max_v = 0
    for i in range(len(input_li)):
        li[input_li[i][0]] = input_li[i][1]
        if max_v < input_li[i][0]:
            max_v = input_li[i][0]
    i = max_v
    while i >= 0:
        if not i % 2 and li[i]:
            if N+1 == i+1:
                li[i//2] = li[i]
            elif N+1> i+1:
                li[i//2] = li[i] + li[i+1]
        i -= 1

    print(li[L])
# 트리를 만들고 리프노드의 값을 채워줌
# 인덱스를 n까지 잡으면 리프노드에 해당
# 부모노드는 자식노드의 합이므로 부모를 찾아가면서 값을 더해줌
# 후위순회하며 값 더하기