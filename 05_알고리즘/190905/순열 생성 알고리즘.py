arr = [1, 2, 3, 4, 5]
N = 5
R = 3



def perm_r_3(k):
    if k == R:
        print(arr[0], arr[1], arr[2])
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm_r_3(k + 1)
            arr[k], arr[i] = arr[i], arr[k]

perm_r_3(0)
print(arr)