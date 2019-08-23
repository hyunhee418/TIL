import sys
sys.stdin = open("input (2).txt", "r")

def max_length(a):
    max_l = 0
    for ele in a:
        if len(ele) > max_l:
            max_1 = len(ele)
    return max_1

for tc in range(1, 11):
    N = int(input())
    print("#%d" %(tc), end=" ")
    li = [[i for i in input()] for _ in range(100)]
    result = []
    re = []



    for length in range(3, 100):
        for y in range(len(li)):
            for move in range(len(li[0]) - length + 1):
                if length % 2 == 1 and li[y][move:move + (length // 2)][::-1] == li[y][move + int(length / 2) + 1:move + length]:
                    result.append(li[y][move:move + length])
                elif length % 2 == 0 and li[y][move:move + (length // 2)][::-1] == li[y][move + int(length / 2):move + length]:
                    result.append(li[y][move:move + length])

        for x in range(len(li[0])):
            sero = [1]
            for i in range(length - 1):
                sero.append(li[i][x])
            for move in range(length, len(li) + 1):
                sero.pop(0)
                sero.append(li[move - 1][x])
                if length % 2 == 1 and sero[:(length // 2)][::-1] == sero[length // 2 + 1:length]:
                    for i in sero:
                        re.append(i)
                    result.append(re)
                    re = []

                elif length % 2 == 0 and sero[:(length // 2)][::-1] == sero[length // 2:length]:
                    for i in sero:
                        re.append(i)
                    result.append(re)
                    re = []

    print(max_length(result))

