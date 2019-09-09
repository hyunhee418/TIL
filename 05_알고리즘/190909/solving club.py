import sys
sys.stdin = open('input.txt', 'r')

def func(x):
    if x:
        func(li[x][2])
        print(li[x][1], end='')
        func(li[x][3])

for tc in range(1, 11):
    print('#%d' %(tc), end=' ')
    N = int(input())
    li = [list(input().split()) for _ in range(N)]
    li.insert(0, [0, 0, 0, 0])
    for check in range(1, N+1):
        if len(li[check]) == 4:
            li[check][0] = int(li[check][0])
            li[check][2] = int(li[check][2])
            li[check][3] = int(li[check][3])
        if len(li[check]) == 3:
            li[check][0] = int(li[check][0])
            li[check][2] = int(li[check][2])
            li[check].append(0)
        if len(li[check]) == 2:
            li[check][0] = int(li[check][0])
            li[check].extend([0, 0])

    func(1)
    print()