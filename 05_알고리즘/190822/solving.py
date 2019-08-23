import sys
sys.stdin = open("input (2).txt", "r")

for tc in range(1, 3):
    N, S = map(int, input().split())
    li_input = list(map(int, input().split()))
    start = []
    check = []

    for i in range(0, N, 2):
        for j in range(1, N, 2):
            if li_input[i] ==li_input[j]:
                check.append(li_input[i])
    for s in range(0, N, 2):


    for x in range(0, N, 2):
        if li_input[x] in check:
            print(li_input[x])
            check.pop(check.index(li_input[x]))
    print(start)
    # j = start[0]
    # result = [j]
    # while len(result) == N:
    #     for idx in range(1, N, 2):
    #         if j == li_input[idx]:
    #             j = li_input[idx+1]
    #             result.append(j)
    #             li_input.pop(idx)
    #             li_input.pop(idx)
    #         else:
    #             j = start[c]
    #             c += 1
    #
    # print(result)

#     visited = [0]*N
#     visited[j] += 1
#     c = 1
#     result = [j+1]
#     while sum(visited) != N:
#         for i in range(N):
#             if li[j][i] == 1 and visited[i] == 0:
#                 li[j][i] = 0
#                 visited[i] = 1
#                 result.append(i+1)
#                 j = i
#         if len(start) > c:
#             j = start[c]
#             start.pop(0)
#             c += 1
#         if len(start) == 0:
#             for x in range(N):
#                 su = 0
#                 for y in range(N):
#                     su += li[y][x]
#                 if su == 0:
#                     start.append(x)
#         if len(start) < c:
#             j = start[0]
#             c = 0
#
#     print(result)