import sys
sys.stdin = open("4861.txt", "r")

T = int(input())
for tc in range(1, T+1):
    print("#%d" %(tc), end=" ")
    a, b = map(int, input().split())
    li = []
    for _ in range(a):
        li.append(str(input()))

    result = [0]*b

    for y in range(len(li)):
        for x in range(int(len(li[0])/2)):
            if li[y][x] == li[y][b-x-1]:
                result[x] = li[y][x]
                result[b-x-1] = li[y][x]
            else:
                y += 1
            if len(result) == int(b/2):
                break

    for x in range(len(li[0])):
        for y in range(len(li)):
            if li[y][x] == li[b-y-1][x]:
                result.append(li[y][x])

            if len(result) == b:
                break

    print(result)