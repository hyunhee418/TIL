import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, 11):
    print('#%d' %(tc), end=' ')
    N = int(input())
    li = []
    num = [0]*(N+1)
    for _ in range(N):
        x = list(input().split())
        if len(x) == 4:
            li.append(x)
        else:
            num[int(x[0])] = int(x[1])
    for i in range(len(li)-1, -1, -1):
        if li[i][1] == '+':
            num[int(li[i][0])] = num[int(li[i][2])] + num[int(li[i][3])]

        elif li[i][1] == '-':
            num[int(li[i][0])] = num[int(li[i][2])] - num[int(li[i][3])]

        elif li[i][1] == '*':
            num[int(li[i][0])] = num[int(li[i][2])] * num[int(li[i][3])]

        elif li[i][1] == '/':
            num[int(li[i][0])] = num[int(li[i][2])] / num[int(li[i][3])]

    print(int(num[1]))