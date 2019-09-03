import sys
sys.stdin = open('incr.txt', 'r')



def mono(a):
    for i in range(1, len(a)):
        if int(a[i-1]) > int(a[i]):
            return False
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    value = 0
    for i in range(N):
        for j in range(i, N):
            if i != j:
                if mono(str(li[i] * li[j])) and value < li[i] * li[j] and 10 <= li[i] * li[j]:
                    value = li[i] * li[j]

    if value:
        print('#%d %d' %(tc, value))
    else:
        print('#%d %d' %(tc, -1))