import sys
sys.stdin = open('d.txt', 'r')

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
li.sort(key=lambda x:x[1])
time = [0]*N
cnt = 0
time[0] = li[0]
x = 0
while x != N-1:
    for x in range(len(time)):
        if time[x]:
            for i in range(x, len(li)):
                if time[x][1] <= li[i][0]:
                    time[i] = li[i]
                    cnt += 1
                    break
print(cnt+1)