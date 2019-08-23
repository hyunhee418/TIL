a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def max_sum_h(a):
    max_h = a[0]
    sum = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            sum += a[i][j]
        if sum > max_h:
            max_h = sum

def construct_cadidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input):
    c = [0]* maxcandidates
    li = []
    if k == input:
        li.append(a, k)
        return li
    else:
        k += 1
        ncadidates = construct_cadidates(a, k, input, c)
        for i in range(ncadidates):
            a[k] = c[i]
            backtrack(a, k, input)

maxcandidates = 100


print(backtrack(a, 0, 10))