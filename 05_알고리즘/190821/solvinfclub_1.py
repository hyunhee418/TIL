import sys
sys.stdin = open("input.txt")

for tc in range(10):
    N = int(input())
    li = [[i for i in input()] for _ in range(8)]
    result = []
    sero = []
    count = 0

    for y in range(len(li)):
        for move in range(len(li[0]) - N + 1):
            if N % 2 == 1 and li[y][move:move + (N // 2)][::-1] == li[y][move + int(N / 2) + 1:move + N]:
                result.append(li[y][move:move + N])
            elif N % 2 == 0 and li[y][move:move + (N // 2)][::-1] == li[y][move + int(N / 2):move + N]:
                result.append(li[y][move:move + N])
    print(len(result))

    for y in range(len(li)):
        for move in range(len(li[0]) - N + 1):
            if N % 2 == 1 and li[y][move:move + (N // 2)][::-1] == li[y][move + int(N / 2) + 1:move + N]:
                result.append(li[y][move:move + N])
            elif N % 2 == 0 and li[y][move:move + (N // 2)][::-1] == li[y][move + int(N / 2):move + N]:
                result.append(li[y][move:move + N])
    print(len(result))






    # for x in range(len(li[0])):
    #     sero = [1]
    #     for i in range(N - 1):
    #         sero.append(li[i][x])
    #     for move in range(N, len(li)):
    #         sero.pop(0)
    #         sero.append(li[move][x])
    #         if N % 2 == 1 and sero[:(N // 2)][::-1] == sero[N // 2 + 1:N]:
    #             result.append(sero)
    #             print(sero)
    #         elif N % 2 == 0 and sero[:(N // 2)][::-1] == sero[N // 2:N]:
    #             result.append(sero)
    #             print(sero)
    #         sero.pop(0)
    #         sero.append(li[move][x])
    #
    # print(len(result))