input = '4 2'

def perm(arr, k, x, empty):
    global res1
    if k == m:
        res = []
        for i in range(k):
            res.append(empty[i])
        res1.append(res)
    else:
        for i in range(x, n+1):
            empty.append(i)
            perm(arr, k+1, i, empty)
            empty.pop()

n, m = map(int, input.split())
arr= [0] * n
for i in range(n):
    arr[i] = i+1
res1 = []
perm(arr, 0, 1, [])
print(res1)