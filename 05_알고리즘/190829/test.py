import sys
sys.stdin = open('s.txt', 'r')

arr = [list(map(int, input().split())) for _ in range(3)]
print(arr)

def find(i, j):
    width = 0
    area = 0
    for h in range(i, len(arr)):
        if arr[h][0] == 0:
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

print(find(0, 0))