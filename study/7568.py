import sys
sys.stdin = open('7568.txt', 'r')

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
lank = [[] for _ in range(N)]
for i in range(N):
    cnt = 0
    for id in range(N):
        if (li[i][0] < li[id][0] and li[i][1] < li[id][1]):
            cnt += 1
    print(cnt+1, end=' ')


# 117592 KB 116 ms