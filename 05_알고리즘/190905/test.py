import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())
for tc in range(1, 2):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    li=[0,1,2]
    for i in range(len(li)):
        print(arr[i][li[i]], end=' ')
    print()