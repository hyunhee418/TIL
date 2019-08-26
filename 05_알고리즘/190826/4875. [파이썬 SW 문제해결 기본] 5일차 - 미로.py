import sys
sys.stdin = open('input_10_100.txt', 'r')

T = int(input())


# def backtracking(li, i, j):
#     d = [-1, 1]
#     result = 0
#     for id in range(len(d)):
#         if result == 1:
#             return 1
#         else:
#             if i + 1 < len(li) and li[i + 1][j] == '2':
#                 result = 1
#             elif j + 1 < len(li[0]) and li[i][j + d[id]] == '2':
#                 result = 1
#             elif 0 <= i - 1 and li[i - 1][j] == '2':
#                 result = 1
#             elif 0 <= j - 1 and li[i][j - 1] == '2':
#                 result = 1
#             elif i + 1 < len(li) and li[i + 1][j] == '0':
#                 li[i + 1][j] = 1
#                 return backtracking(li, i + 1, j)
#             elif 0 <= i - 1 and li[i - 1][j] == '0':
#                 li[i - 1][j] = 1
#                 return backtracking(li, i - 1, j)
#             elif j + 1 < len(li[0]) and li[i][j + 1] == '0':
#                 li[i][j + 1] = 1
#                 return backtracking(li, i, j + 1)
#             elif 0 <= j - 1 and li[i][j - 1] == '0':
#                 li[i][j - 1] = 1
#                 return backtracking(li, i, j - 1)
#     else:
#         result = 0
#     return result
#
# def backtracking(li, i, j):
#     d = [-1, 1]
#
#     for id in range(len(d)):
#         if stack == []:
#             return 0
#         if i + 1 < len(li) and li[i + 1][j] == '2':
#             return 1
#         elif j + 1 < len(li[0]) and li[i][j + d[id]] == '2':
#             return 1
#         elif 0 <= i - 1 and li[i - 1][j] == '2':
#             return 1
#         elif 0 <= j - 1 and li[i][j - 1] == '2':
#             return 1
#         elif i + 1 < len(li) and li[i + 1][j] == '0':
#             li[i + 1][j] = 1
#             stack.append((i + 1, j))
#             return backtracking(li, i + 1, j)
#         elif 0 <= i - 1 and li[i - 1][j] == '0':
#             li[i - 1][j] = 1
#             stack.append((i - 1, j))
#             return backtracking(li, i - 1, j)
#         elif j + 1 < len(li[0]) and li[i][j + 1] == '0':
#             li[i][j + 1] = 1
#             stack.append((i, j + 1))
#             return backtracking(li, i, j + 1)
#         elif 0 <= j - 1 and li[i][j - 1] == '0':
#             li[i][j - 1] = 1
#             stack.append((i, j - 1))
#             return backtracking(li, i, j - 1)
#     else:
#         i, j = stack.pop()
#         return backtracking(li, i, j)

def dfs(li, i, j):


#           if i + 1 < len(li) and li[i + 1][j] == '2':
#             return 1
#         elif j + 1 < len(li[0]) and li[i][j + d[id]] == '2':
#             return 1
#         elif 0 <= i - 1 and li[i - 1][j] == '2':
#             return 1
#         elif 0 <= j - 1 and li[i][j - 1] == '2':
#             return 1
#         elif i + 1 < len(li) and li[i + 1][j] == '0':
#             li[i + 1][j] = 1
#             stack.append((i + 1, j))
#             return backtracking(li, i + 1, j)
#         elif 0 <= i - 1 and li[i - 1][j] == '0':
#             li[i - 1][j] = 1
#             stack.append((i - 1, j))
#             return backtracking(li, i - 1, j)
#         elif j + 1 < len(li[0]) and li[i][j + 1] == '0':
#             li[i][j + 1] = 1
#             stack.append((i, j + 1))
#             return backtracking(li, i, j + 1)
#         elif 0 <= j - 1 and li[i][j - 1] == '0':
#             li[i][j - 1] = 1
#             stack.append((i, j - 1))
#             return backtracking(li, i, j - 1)
#     else:
#         i, j = stack.pop()
#         return backtracking(li, i, j)


for tc in range(1, T + 1):
    f = 0
    N = int(input())
    li = [[s for s in input()] for _ in range(N)]
    for x in range(len(li)):
        for y in range(len(li[0])):
            if li[x][y] == '3':
                stack = [(0, 0), (x, y)]
                result = dfs(li, x, y)
                print("#%d %d" %(tc, result))
                f = 1
                break
        if f:
            break