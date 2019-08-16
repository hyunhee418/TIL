ary = [[1, 2, 3, 4, 5],
       [6, 8, 10, 12, 14],
       [15, 18, 21, 24, 27],
       [28, 32, 36, 40, 44],
       [45, 50, 55, 60, 65]]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
li = []
result = []
for x in range(len(ary)):
    for y in range(len(ary[0])):
        for idx in range(len(dx)):
            if x + dx[idx] >= 0 and y + dy[idx] >= 0 and x + dx[idx] < len(ary) and y + dy[idx] < len(ary[0]):
                li.append(abs(ary[x][y] - ary[x + dx[idx]][y + dy[idx]]))
                result.append(abs(ary[x][y] - ary[x + dx[idx]][y + dy[idx]]))
        print(sum(li))
        li = []
print(sum(result))


