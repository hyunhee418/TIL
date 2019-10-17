import sys
sys.stdin = open('2630.txt', 'r')

def check(li):
    for x in range(len(li)):
        for y in range(len(li[0])):
            if li[x][y] == 0:
                return False
    return True

def isEnd(li):
    for x in range(len(li)):
        for y in range(len(li[0])):
            if li[x][y]:
                return True
    return False

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
for i in range(N):
    if N == 1:
        break
    N = N//2
    cnt += 1

while isEnd(arr):
    n = 0
    N = N // 2
    while:
        ar = [[0] * N for _ in range(N)]
