import sys
sys.stdin = open("baekjoon_2.txt", "r")



li = [[0 for _ in range(1, 101)] for _ in range(1, 101)]

li_2 = [list(map(int, input().split())) for _ in range(4)]

for i in range(len(li_2)):
    for s in range(li_2[i][0], li_2[i][2]):
        for j in range(li_2[i][1], li_2[i][3]):
            li[s][j] = 1

count = 0
for x in range(0, 100):
    for y in range(0, 100):
        if li[x][y] == 1:
            count += 1
print(count)