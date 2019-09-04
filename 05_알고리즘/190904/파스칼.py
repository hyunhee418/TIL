import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print('#%d' %(tc))
    N = int(input())
    result = []
    for i in range(N):
        l = [1]
        if i == 0:
            result.append([1])
        else:
            for n in range(i-1):
                l.append(result[i-1][n]+result[i-1][n+1])
            l.append(1)
            result.append(l)
    for y in range(len(result)):
        for x in range(len(result[y])):
            print(result[y][x], end=' ')
        print()