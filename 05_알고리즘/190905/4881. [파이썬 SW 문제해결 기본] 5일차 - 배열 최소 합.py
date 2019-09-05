import sys
sys.stdin = open('sample_input.txt', 'r')


def perm_r_3(k, s):
    global li, min_v

    if s >= min_v:
        return
    if k == len(li) - 1:
        sum = 0
        for i in range(len(li)):
            sum += arr[i][li[i]]
        if sum < min_v:
            min_v = sum
        return
    else:
        for i in range(k, N):
            li[k], li[i] = li[i], li[k]
            perm_r_3(k + 1, s+arr[k][li[k]])
            li[k], li[i] = li[i], li[k]


for tc in range(1, int(input()) + 1):
    print('#%d' %(tc), end=' ')
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    li = [num for num in range(N)]
    min_v = 100
    perm_r_3(0, 0)
    print(min_v)

# def func(k):
#     li = []
#     for i in range(1, (N*N)+1):
#         li.append(i)
#     if k == N:
#         print(li[0])
#     else:
#         for i in range(len(li)):
#             if i % N == 0:
#                 for j in range(k, i+N):
#                     li[k], li[j] = li[j], li[k]
#                     func(k+1)
#                     li[k], li[j] = li[j], li[k]
# func(0)



