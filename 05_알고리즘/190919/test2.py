arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def powerset(k, N):
    if k == N:
        if sum(t) == 10 and sorted(t) not in result:
            print(t)
            result.append(sorted(t))
    else:
        for i in range(len(arr)):
            if visited[i]:
                continue
            t[k] = arr[i]
            visited[i] = 1
            powerset(k+1, N)
            visited[i] = 0

result = []
visited = [0] * len(arr)
for N in range(1, len(arr)+1):
    t = [0] * N
    powerset(0, N)