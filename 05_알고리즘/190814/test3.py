li = [[9, 20, 2, 18, 11],
      [19, 1, 25, 3, 21],
      [8, 24, 10, 17, 7],
      [15, 4, 16, 5, 6],
      [12, 13, 22, 23, 14]]
li_2 = []

def min_hh(a):
    min_num = a[0]
    for i in a:
        if i < min_num:
            min_num = i
    return min_num

for x in range(len(li)):
    print(min_hh(min_hh(li[x])))
        # for i in range(min_x + 1, len(li)):
        # for j in range(min_y + 1, len(li[0])):
        #     if li[min_x][j] < li[min_x][min_y]:
        #         min_y = j
        # li[min_x][y], li[min_x][min_y] = li[min_x][min_y], li[min_x][y]



            # if li[i][0] < li[min_x][min_y]:
            #    min_x = i
            # li[i][0], li[min_x][min_y] = li[min_x][min_y], li[i][0]
            # print(li)
print(li)