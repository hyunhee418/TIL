import sys
sys.stdin = open('sample_input_pizza.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print('#%d' %(tc), end=' ')
    N, M = map(int, input().split())
    li_input = list(map(int, input().split()))
    q = []
    li = []
    for i in range(len(li_input)):
        li.append([li_input[i], i])
    for _ in range(N):
        q.append(li.pop(0))
    while len(q) != 1:
        a = q.pop(0)
        a[0] = a[0]//2
        if a[0] == 0:
            if li != []:
                q.append(li.pop(0))
        else:
            q.append(a)
    print(q.pop()[1]+1)