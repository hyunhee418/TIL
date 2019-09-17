li = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

def powerset(li):
    r = [[]]
    print([])
    for ele in li:
        ele = [x +[ele] for x in r]
        for i in range(len(ele)):
            if sum(ele[i]) == 0:
                print(ele[i])
        r += ele
    return r

for i in powerset(li):
    if sum(i) == 0:
        print(i)



def comb(n, r):
    if r == 0:
        if sum(tr) == 0:
            print(tr)
    elif n < r:
        return
    else:
        tr[r-1] = li[n-1]
        comb(n-1, r-1)
        comb(n-1, r)

for i in range(len(li)):
    tr = [0]*i
    comb(len(li), i)





