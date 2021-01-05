import sys
sys.stdin = open("input.txt", "r")
ii = 0
arr = {}
def tree(v, i, ii):
    if arr[i][2]:
        if arr[i][2] > v:
            if not arr[i][0]:
                arr[i][0] = ii
            tree(v, arr[i][0], ii)

        else:
            if not arr[i][1]:
                arr[i][1] = ii
            tree(v, arr[i][1], ii)
    else:
        arr[i][2] = v
def printTree(ddi, d):
    if arr[ddi][0]:
        printTree(arr[ddi][0], 0)
    if arr[ddi][1]:
        printTree(arr[ddi][1], 1)
    print(arr[ddi][2])
while True:
    try:
        arr[ii] = [0,0,0]
        tree(int(input()), 0, ii)
        ii+=1
    except:
        break

printTree(0, 0)