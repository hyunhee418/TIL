import sys
sys.stdin = open("GNS_test_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    S, N = input().split()
    print(S, end=" ")
    N = int(N)
    num_li = []
    values = list(map(str, input().split()))
    li = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    # for i in range(N-1):
    #     min = i
    #     for idx in range(i+1, N):
    #         if li.index(values[min]) > li.index(values[idx]):
    #             min = idx
    #     values[i], values[min] = values[min], values[i]
    #
    # print(S, ' '.join(values))
    for i in range(len(li)):
        print((li[i]+" ")*(values.count(li[i])), end = " ")

    print()