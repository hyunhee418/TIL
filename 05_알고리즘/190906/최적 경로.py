import sys
sys.stdin = open('input.txt', 'r')

def length(lli):
    sum_c = 0
    for i in range(len(lli)-1):
        sum_c += abs(li[lli[i]] - li[lli[i+1]]) + abs(li[lli[i]+1] - li[lli[i+1]+1])
    return sum_c

def func(k):
    global min_sum
    if k == N:
        lli = []
        for i in range(k):
            lli.append(l[i]*2 + 4)
        lli.insert(0, 0)
        lli.append(2)
        a = length(lli)
        if a < min_sum:
            min_sum = a
    else:
        for i in range(k, len(l)):
            l[i], l[k] = l[k], l[i]
            func(k+1)
            l[i], l[k] = l[k], l[i]
T = int(input())
for tc in range(1, 1+T):
    print('#%d' %(tc), end=' ')
    N = int(input())
    l = [i for i in range(N)]
    li = list(map(int, input().split()))
    lli = []
    min_sum = 1000
    result = []
    func(0)
    print(min_sum)


        # for s in range(len(visited)):
        #     if visited[s]:
        #         visited[s] +=  abs(x - li[i]) + abs(y - li[i + 1])