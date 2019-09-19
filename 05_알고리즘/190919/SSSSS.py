

def power_set_r(k):
    if k == N: print(a)
    else:
        a[k] = 1; power_set_r(k + 1)
        a[k] = 0; power_set_r(k + 1)

N = 3
a = [0] * N
power_set_r(0)