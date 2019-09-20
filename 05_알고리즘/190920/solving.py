import sys
sys.stdin = open('sample_input.txt', 'r')

for tc in range(1, 1+int(input())):
    print('#%d' %(tc), end=' ')
    N, M = map(int, input().split())
    li =  [int(input()) for _ in range(N)]
    time = 0
    while M > 0:
        time += 1
        for wait_time in li:
            if time % wait_time == 0:
                M -= 1
    print(time)