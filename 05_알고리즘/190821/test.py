l = [1,2,3,4,5]
N = 3
for move in range(len(l) - N + 1):
    print(l[move + int(N / 2):move + N - 1])