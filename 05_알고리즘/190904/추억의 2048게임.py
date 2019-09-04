import sys
sys.stdin = open('s_input (2).txt', 'r')


T = int(input())
for tc in range(1, T+1):
    print('#%d' %(tc))
    li = input().split()
    arr = [list(map(int, input().split())) for _ in range(int(li[0]))]
    if li[1] == 'up' or li[1] == 'left':
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if li[1] == 'up':
                    dy = 1
                    if arr[i][j] == 0 and i+dy < len(arr):
                        while i+dy < len(arr)-1 and arr[i+dy][j] == 0:
                            dy += 1
                        arr[i][j] = arr[i+dy][j]
                        arr[i+dy][j] = 0
                        dy = 1
                    while i+dy < len(arr):
                        if arr[i+dy][j] != 0 and arr[i+dy][j] != arr[i][j]:
                            break
                        elif arr[i+dy][j] == arr[i][j]:
                            arr[i][j] = arr[i][j]*2
                            arr[i+dy][j] = 0
                            break
                        dy += 1
                elif li[1] == 'left':
                    dx = 1
                    if arr[i][j] == 0 and j + dx < len(arr):
                        while j + dx < len(arr) - 1 and arr[i][j+dx] == 0:
                            dx += 1
                        arr[i][j] = arr[i][j + dx]
                        arr[i][j + dx] = 0
                        dx = 1
                    while j + dx < len(arr):
                        if arr[i][j + dx] != 0 and arr[i][j + dx] != arr[i][j]:
                            break
                        elif arr[i][j + dx] == arr[i][j]:
                            arr[i][j] = arr[i][j] * 2
                            arr[i][j + dx] = 0
                            break
                        dx += 1
    elif li[1] == 'down' or li[1] == 'right':
        for i in range(len(arr)-1, -1, -1):
            for j in range(len(arr[0])-1, -1, -1):
                if li[1] == 'down':
                    dy = -1
                    if arr[i][j] == 0 and 0 <= i+dy:
                        while 0 <= i+dy and arr[i+dy][j] == 0:
                            dy += -1
                        if 0 <= i+dy:

                            arr[i][j] = arr[i+dy][j]
                            arr[i+dy][j] = 0
                            dy = -1
                    while 0 <= i+dy:
                        if arr[i+dy][j] != 0 and arr[i+dy][j] != arr[i][j]:
                            break
                        elif arr[i+dy][j] == arr[i][j]:
                            arr[i][j] = arr[i][j]*2
                            arr[i+dy][j] = 0
                            break
                        dy += -1

                elif li[1] == 'right':
                    dx = -1
                    if arr[i][j] == 0 and 0 <= j+dx:
                        while 0 <= j+dx and arr[i][j+dx] == 0:
                            dx += -1
                        if 0 <= j+dx:
                            arr[i][j] = arr[i][j+dx]
                            arr[i][j+dx] = 0
                            dx = -1
                    while 0 <= j+dx:
                        if arr[i][j+dx] != 0 and arr[i][j+dx] != arr[i][j]:
                            break
                        elif arr[i][j+dx] == arr[i][j]:
                            arr[i][j] = arr[i][j]*2
                            arr[i][j + dx] = 0
                            break
                        dx += -1

    for y in range(len(arr)):
        for x in range(len(arr[0])):
            print(arr[y][x] ,end=' ')
        print()