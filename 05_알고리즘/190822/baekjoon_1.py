import sys
sys.stdin = open("baekjoon_1.txt", "r")
li = [[0 for _ in range(102)] for _ in range(102)]
N = int(input())
li_2 = [list(map(int, input().split())) for _ in range(N)]

for ele in range(len(li_2)):
    li_2[ele][2] = li_2[ele][0] + li_2[ele][2]
    li_2[ele][3] = li_2[ele][1] + li_2[ele][3]
print(li_2)
for number in range(N):
    for j in range(li_2[number][1], li_2[number][3]):
        for i in range(li_2[number][0], li_2[number][2]):
            li[j][i] = 10**(number+1)
print(li)
for number in range(1, N+1):
    count = 0
    find = 0
    for x in range(102):
        for y in range(102):
            if li[x][y] == 10**(number):
                count += 1
    print(count)




# li = [list(map(int, input().split())) for _ in range(N)]
# print(li)
# for ele in range(len(li)):
#     li[ele][2] = li[ele][0] + li[ele][2]
#     li[ele][3] = li[ele][1] + li[ele][3]
# # print(li)
# for point in range(len(li)):
#     result = 0
#     result += (li[point][2] - li[point][0]) * (li[point][3] - li[point][1])
#     # print(result)
#
#     for ele_li in li[point+1:]:
#         l = [0]*4
#         for i in range(4):
#             l[i] = li[point][i]
#         for i in range(0, 4, 2):
#             for j in range(1, 4, 2):
#                 if ele_li[i] in range(li[point][0], li[point][2]) and ele_li[j] in range(li[point][1], li[point][3]):
#                     if ele_li[0] > li[point][0]:
#                         l[0] = ele_li[0]
#                     if ele_li[1] > li[point][1]:
#                         l[1] = ele_li[1]
#                     if ele_li[2] < li[point][2]:
#                         l[2] = ele_li[2]
#                     if ele_li[3] < li[point][3]:
#                         l[3] = ele_li[3]
#         # print(l)
#         if l != li:
#             result -= (l[2] - l[0]) * (l[3] - l[1])
#     print(result)
