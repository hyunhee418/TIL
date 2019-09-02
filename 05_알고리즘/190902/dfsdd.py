node = [[1, 2], [3, 4], [5, 6, 7]]

def dfs(x):
    print(x)
    if node[x]:
        for i in range(len(node[x])):
            try:
                dfs(node[x][i])

            except IndexError:
                pass
dfs(0)
