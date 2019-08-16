import sys
sys.stdin = open("input_solving.txt", "r")

def count_h(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] == b:
            count += 1
    return count



T = int(input())



for tc in range(1, T+1):
    N = int(input())
    L = list(map(int, input().split()))
    for he in range(0, len(L), 2):
        if L.count(L[he]) == 1:
            L[he], L[0] = L[0], L[he]
            L[1], L[he+1] = L[he+1], L[1]
    print(L)

    for i in range(2, len(L), 2):
        for j in range(1, len(L)-2, 2):
            if L[i] == L[j]:
                L[i], L[j+1] = L[j], L[i+1]
                L[i+1], L[j+2] = L[j+2], L[i+1]


    print(L)