import sys
sys.stdin = open("sample_input.txt", "r")

def paper(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n >= 3:
        return (paper(n-1) + (2 * paper(n-2)))

    # if n == 1:
    #     return 1
    # if n == 2:
    #     return 3
    # if n % 2:
    #     return 2 * paper(n-1) -1
    # if n % 2 == 0:
    #     return 2 * paper(n-1) +1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print("#%d %d" %(tc, paper(N//10)))