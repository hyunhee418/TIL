def sum_h(l):
    sum_h = 0
    for i in range(len(l)):
        for j in range(len(l)):
            sum_h += l[i][j]
    return sum_h

visited = [[0 for _ in range(10)] for _ in range(10)]

if sum_h(visited) == 0:
    print(True)
else:
    print(False)