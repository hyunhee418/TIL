import sys
sys.stdin = open("4861.txt", "r")

T = int(input())
for tc in range(1, T+1):
    print("#%d" %(tc), end=" ")
    a, b = map(int, input().split())
    li = []
    for _ in range(a):
        li.append(str(input()))

    result = []
    count = 0

    for y in range(len(li)):
        for x in range(len(li[0])):
            if li[y][x] == li[y][x+b-]:
                result.append(li[y][x])
                count += 1
            elif li[y][x] == li[y + b-1][x]:
                result.append(li[y][x])
                count += 1
            if count == int(b/2):
                print(result)
                break
            else:
                count = 0
