import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    V, E = map(int, input().split())
    input_li = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    print(input_li)
    arr = [[] for _ in range(V+1)]
    for i in range(len(input_li)):
        arr[input_li[i][0]].append(input_li[i][1])

    