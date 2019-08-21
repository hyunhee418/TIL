T = int(input())
for tc in range(1, T+1):
    print("#%d" %(tc), end=" ")
    str1 = str(input())
    str2 = str(input())
    i = len(str1)-1
    j = len(str1)-1

    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            if i == 0:
                print(1)
                break
            i += -1
            j += -1
        else:
            i += -1
            if i == 0:
                i = len(str1)-1
                j += len(str1)
                if j >= len(str2):
                    print(0)
                    break

                    while y < len(li) and 0 in result:
                        x = 0
                        y += 1
                        while x < int((len(li[0])) / 2) and 0 in result and y < len(li):
                            s = 0
                            for i in range(0, int(b / 2 + 1)):
                                if y < len(li) and x + (b - 1) < len(li[0]) and li[y][x] == li[y][x + (b - 1)] and li[y][x + i] == li[y][x + b - 1 - i]:
                                    result[i] = li[y][x]
                                    result[b - i - 1] = li[y][x]
                                    x += 1
                                else:
                                    x += 1
                    while x_1 < len(li[0]):
                        y_1 = 0
                        x_1 += 1
                        while y_1 < int((len(li)) / 2):
                            if x_1 > len(li[0]):
                                break
                            if x_1 < len(li[0]) and y_1 + (b - 1) < len(li) and li[y_1][x_1] == \
                                    li[y_1 + (b - 1)][x_1] and li[y_1 + 1][x_1] == li[y_1 + b - 2][x_1]:
                                for i in range(int(b / 2) + 1):
                                    result[i] = li[y_1][x_1]
                                    result[b - i - 1] = li[y_1][x_1]
                                    y_1 += 1
                            else:
                                y_1 += 1
