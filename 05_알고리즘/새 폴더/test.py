import sys
sys.stdin = open('sample_input_A1.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    print("#%d"%(tc), end=' ')
    N = int(input())
    l = list(map(int, input().split()))
    count = 0
    if sorted(l) == l:
        print(count)

def shuffle():
    r1 = (N/2)
    r2 = (N/2 + 1)
    if 
