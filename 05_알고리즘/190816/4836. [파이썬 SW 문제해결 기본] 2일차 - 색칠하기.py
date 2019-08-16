import sys
sys.stdin = open("input_color.txt", "r")

def range_h(a, b):
    if a > b:
        return range(b, a + 1)
    else:
        return range(a, b + 1)

T = int(input())
for tc in range(1, T+1):
    count = 0
    N = int(input())
    li = [list(map(int, input().split())) for S in range(N)]
    coordinates = [[0 for _ in range(10)] for _ in range(10)]
    for idx in range(len(li)):
        for i in range_h(li[idx][2], li[idx][0]):
            for j in range_h(li[idx][1], li[idx][3]):
                coordinates[j][i] += li[idx][4]
    for x in range(len(coordinates)):
        for y in range(len(coordinates[0])):
            if coordinates[x][y] >= 3:
                count += 1

    print("#%d %d" %(tc, count))