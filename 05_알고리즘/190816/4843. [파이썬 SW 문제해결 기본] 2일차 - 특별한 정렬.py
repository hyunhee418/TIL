import sys
sys.stdin = open("input_sp.txt", "r")


T = int(input())
for tc in range(1, T+1):
    print("#%d" %(tc), end=" ")
    N = int(input())
    L = list(map(int, input().split()))
    for idx in range(N-1):
        min = idx
        for j in range(idx+1, N):
            if L[min] > L[j]:
                min = j
        L[idx], L[min] = L[min], L[idx]
    i_li = [i for i in range(N)]
    for i in range(5):
        print(L[-(i+1)], end=" ")
        print(L[i], end=" ")
    print()