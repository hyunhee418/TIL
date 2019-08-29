import sys
sys.stdin = open('input.txt', 'r')


def find(i, j):
    width = 0
    area = 0
    for h in range(i, len(arr)):
        if arr[h][j] == 0:
            break
        width = 0
        for s in range(j, len(arr[0])):
            if arr[h][s] != 0:
                arr[h][s] = 0
                width += 1
                area += 1
            else:
                break


    return [width, area]


T = int(input())
for tc in range(1, T+1):
    print('#%d' %(tc), end=' ')
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for s in range(len(arr)):
        for h in range(len(arr[s])):
            if arr[s][h] != 0:
                result.append(find(s, h))
    print(len(result), end= " ")
    for re in range(len(result)-1):
        min = re
        for su in range(re+1, len(result)):
            if result[su][1] < result[min][1]:
                min = su
        result[re], result[min] = result[min], result[re]
    for idx in range(len(result)):
        print(result[idx][1] // result[idx][0], end=" ")
        print(result[idx][0], end=" ")
    print()