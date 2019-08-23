import sys
sys.stdin = open("03.txt", "r")

def sum_h(l):
    sum_h = 0
    for i in range(len(l)):
        for j in range(len(l)):
            sum_h += l[i][j]
    return sum_h

T = int(input())
for tc in range(1, T+1):
    print("#%d" %(tc), end=" ")
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    i = 0
    j = 0
    count = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[i][j] = 0
    while sum_h(li) != 0:
        f = 0
        if li[i][j] == 0:
            for i in range(len(li)):
                for j in range(len(li[0])):
                    if li[i][j] != 0:
                        f = 1
                        break
                if f:
                    break

        else:
            li[i][j] = 0
            stack = [(i, j)]
            while stack != []:
                f = 0
                dxy = [0, -1, 1]
                for dy in range(len(dxy)):
                    for dx in range(len(dxy)):
                        if i+dxy[dy] < len(li) and j+dxy[dx] < len(li[0]) and (dxy[dx] != 0 or dxy[dy] != 0) and li[i+dxy[dy]][j+dxy[dx]] != 0:
                            visited[i][j] = 1
                            li[i + dxy[dy]][j + dxy[dx]] = 0
                            i = i+dxy[dy]
                            j = j+dxy[dx]
                            stack.append((i, j))
                            visited[i][j] = 1
                            dx = 0
                            dy = 0
                            f = 1
                    if f:
                        break


                else:
                    a, b = stack.pop()
                    i = a
                    j = b
            count += 1
            f = 0
    print(count)