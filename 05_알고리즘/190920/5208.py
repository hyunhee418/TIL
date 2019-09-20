import sys
sys.stdin = open('sample_input_5208.txt', 'r')

def move(steps, n):
    global min_ch
    if steps >= N-1:
        if n < min_ch:
            min_ch = n
    else:
        for step in range(1, 1+li[steps]):
            if n+1 < min_ch:
                move(steps+step, n+1)
for tc in range(1, 1+int(input())):
    print('#%d' %(tc), end=' ')
    li = list(map(int, input().split()))
    li.append(0)
    N = li.pop(0)
    min_ch = 100
    move(0, 0)
    print(min_ch-1)

