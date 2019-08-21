import sys
sys.stdin = open("4864.txt", "r")

T = int(input())
for tc in range(1, T+1):
    print("#%d" %(tc), end=" ")
    str1 = str(input())
    str2 = str(input())
    i = 0
    j = 0
    while j < len(str1) and i < len(str2):
        if str1[j] != str2[i]:
            i = i-j
            j = -1
        i += 1
        j += 1
    if j == len(str1):
        print(1)
    else:
        print(0)