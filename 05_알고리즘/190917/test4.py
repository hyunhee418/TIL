import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

def func1()
for tc in range(1, 1+T):
    print('#%d' %(tc), end=' ')
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    max = 0
    l = [i for i in range(N)]