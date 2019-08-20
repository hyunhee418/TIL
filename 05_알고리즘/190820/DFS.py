input = "1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7"

s = list(map(int, input.split(",")))
se = list(set(sorted(s)))
li = [[0 for _ in range(len(se))] for _ in range(len(se))]
visited = [0] * len(se)
stack = []
for i in range(0, len(s) - 1, 2):
    li[se.index(s[i])][se.index(s[i + 1])] = 1
    li[se.index(s[i + 1])][se.index(s[i])] = 1
li_2 = []
i = 0
string = ""
while sum(visited) < 7:
    for j in range(len(li[0])):
        visited[i] = 1
        if i not in li_2:
            li_2.append(i)
        if li[i][j] != 0 and visited[j] == 0:
            visited[i] = 1
            stack.append(i)
            i = j
            break
    else:
        i = stack.pop()

for idx in li_2:
    string += str(se[idx])
    string += "-"
print(string[:-1])