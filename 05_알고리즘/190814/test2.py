arr = [3, -6, 7, -1, 5, 4]

n = len(arr)
li = []
for i in range(1, 1 << n):
    for j in range(n):
        if i & (1<<j):
            li.append(arr[j])
    if sum(li) == 0:
        print(li)
    li = []
