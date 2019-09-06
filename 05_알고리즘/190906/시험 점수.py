import sys
sys.stdin = open('sample_input.txt', 'r')


# for tc in range(1, int(input())+1):
#     print('#%d' %(tc), end=' ')
#     R = int(input())
#     li_input = list(map(int, input().split()))
#     result = []
#     for i in range(1<<len(li_input)):
#         l = []
#         for j in range(len(li_input)):
#             if i&(1<<j):
#                 l.append(li_input[j])
#         if sum(l) not in result:
#             result.append(sum(l))
#     print(len(result))


def powersetlist(s):
    r = [[]]
    for e in s:
        temp= [x+[e] for x in r]
        r += temp
    return r

for tc in range(1, int(input())+1):
    print('#%d' %(tc), end=' ')
    R = int(input())
    li_input = list(map(int, input().split()))
    result = []
    for ele in powersetlist(li_input):
        if sum(ele) not in result:
            result.append(sum(ele))
    print(len(result))

# for tc in range(1, int(input())+1):
#     print('#%d' %(tc), end=' ')
#     R = int(input())
#     li_input = [[0]*R, list(map(int, input().split()))]
#
#     dx = [0, 0, -1 ,1]
#     dy = [-1, 1, 0, 0]
#     result = []
#     for s in range(len(li_input)):
#         for r in range(len(li_input[0])):
#             que = [(s, r)]
#             visited = [[0]*R for _ in range(2)]
#             visited[s][r] = 1
#             while que != []:
#                 x, y = que.pop()
#                 for i in range(len(dx)):
#                     if 0 <= x+dx[i] < len(li_input) and 0<= y+dy[i] < len(li_input[0]):
#                         if visited[x+dx[i]][y+dy[i]] == 0:
#                             que.append((x+dx[i], y+dy[i]))
#                             visited[x+dx[i]][y+dy[i]] = visited[x][y]+ li_input[x+dx[i]][y+dy[i]]
#                             if visited[x+dx[i]][y+dy[i]] not in result:
#                                 result.append(visited[x+dx[i]][y+dy[i]])
#     print(len(result))