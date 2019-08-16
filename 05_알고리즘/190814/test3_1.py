li = [9, 20, 2, 18, 11]
#


def min_hh(a):
    min_num = a[0]
    for i in a:
        if i < min_num:
            min_num = i
    return min_num
# for i in range(len(li)):
#     min_y = i
#     for j in range(min_y + 1, len(li)):
#         if li[min_y] > li[j]:
#             min_y = j
#     li[i], li[min_y] = li[min_y], li[i]
# print(li)
print(min_hh(li))
# for i in range(len(li) - 1):
#     min_y = i
#     for j in range(i + 1, len(li)):
#         if li[min_y] > li[j]:
#             min_y = j
#     li[i], li[min_y] = li[min_y], li[i]



print(li)