import sys
sys.stdin = open('input.txt', 'r')

password = [[0,0,0,1,1,0,1], [0,0,1,1,0,0,1], [0,0,1,0,0,1,1], [0,1,1,1,1,0,1], [0,1,0,0,0,1,1],
            [0,1,1,0,0,0,1], [0,1,0,1,1,1,1], [0,1,1,1,0,1,1], [0,1,1,0,1,1,1], [0,0,0,1,0,1,1]]

T = int(input())

def isPassword(li):
    sum1 = 0
    sum2 = 0

    if len(li) == 8:
        for i in range(0, 7, 2):
            sum1+=li[i]
        for j in range(1, 7, 2):
            sum2+=li[j]
        if (sum1*3 + sum2 + li[7]) % 10 == 0:
            return True
        else:
            return False
for tc in range(1, 1+T):
    print('#%d' %(tc), end=' ')
    M, N = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(M)]
    code = []
    f = 0
    for i in range(M):
        j = N-1
        while j >= 0:
            if arr[i][j] == 1 and j-6 > 0 and j+1 <= len(arr[0]):
                l = arr[i][j - 6:j + 1]
                if l in password:
                    code.append(password.index(l))
                    for z in range(j-6, j+1):
                        arr[i][z] = 0
                    for s in range(i+1, M):
                        if arr[s][j - 6:j + 1] in password:
                            for z in range(j - 6, j + 1):
                                arr[s][z] = 0
                        else:
                            break
                    j -= 6
                if isPassword(code[::-1]):
                    print(sum(code))
                    f = 1
                    break
            j -= 1
        if f:
            break

    if f == 0:
        print(0)
