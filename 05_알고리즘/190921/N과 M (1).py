import sys
sys.stdin = open('input.txt', 'r')


def perm(k):
    global M, N
    if k == M:
        for h in range(k):
            print(t[h], end=' ')
        print()
    else:
        for i in range(N):
            if visited[i]:
                continue
            t[k] = l[i]
            visited[i] = 1
            perm(k+1)
            visited[i] = 0
N, M = map(int, input().split())
t = [0] * N
visited = [0] * N
l = [i for i in range(1, 1+N)]
perm(0)




# def perm(k):
#     global M, N, result
#     if k == M:
#         for h in range(k):
#             print(l[h], end=' ')
#         print()
#     else:
#         for j in range(k, N):
#             l[k], l[j] = l[j], l[k]
#             perm(k+1)
#             l[k], l[j] = l[j], l[k]
#
# N, M = map(int, input().split())
# result = []
# l = [i for i in range(1, 1+N)]
# perm(0)



# def perm(k):
#     global M, N, result
#     if k == M:
#         li = []
#         for h in range(k):
#             li.append(l[h])
#
#         print(' '.join(map(str, li)))
#     else:
#         for j in range(k, N):
#             l[k], l[j] = l[j], l[k]
#             perm(k+1)
#             l[k], l[j] = l[j], l[k]
