import sys
sys.stdin = open("4864.txt", "r")

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