import sys
sys.stdin = open('char.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    print('#%d' %tc, end=' ')
    li = [[i for i in input()] for _ in range(5)]
    max_len = 0
    for j in range(5):
        if max_len < len(li[j]):
            max_len = len(li[j])
    for j in range(max_len):
        for i in range(5):
            try:
                print(li[i][j], end='')
            except IndexError:
                pass
    print()