import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    print('#%d' %(tc), end=' ')
    N = int(input())
    arr = [[i for i in input()] for _ in range(N)]
    result = 0
    a = N//2
    b = 1
    for i in range(N):
        if i <= N//2:
            for j in range(a, a+b):
                result += int(arr[i][j])
            a -= 1
            b += 2
        elif i == N//2+1:
            a += 2
            b -= 4
            for j in range(a, a+b):
                result += int(arr[i][j])
            a += 1
            b -= 2
        else:
            for j in range(a, a+b):
                result += int(arr[i][j])
            a += 1
            b -= 2
    print(result)