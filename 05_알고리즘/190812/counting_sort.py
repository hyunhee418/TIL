def counting_sort(a,k):
    b = [0] * len(a)
    c = [0] * k

    for i in range (0, len(b)):
        c[a[i]] += 1
    for i in range (1, len(c)):
        c[i] += c[i-1]
    for i in range (len(b)-1, -1, -1 ):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -= 1
    return b

a = [0, 4, 1, 3, 1, 2, 4, 1]
print(counting_sort(a, 5))
