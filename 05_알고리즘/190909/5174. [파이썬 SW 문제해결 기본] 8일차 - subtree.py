import sys
sys.stdin = open('sample_input (2).txt', 'r')

T = int(input())

def func(x):
    if x:
        l.append(x)
        func(arr[x][0])
        func(arr[x][1])

for tc in range(1, 1+T):
    print('#%d' %(tc), end=' ')
    N, M = map(int, input().split())
    input_li = list(map(int, input().split()))
    arr = [[0, 0] for _ in range(max(input_li)+1)]
    l = []
    for i in range(0, len(input_li)-1, 2):
        if not arr[input_li[i]][0]:
            arr[input_li[i]][0] = input_li[i+1]
        else:
            arr[input_li[i]][1] = input_li[i+1]
    func(M)
    print(len(l))