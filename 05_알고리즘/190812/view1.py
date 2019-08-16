import sys
sys.stdin = open("input.txt", "r")

def find(N, H):
    count = 0
    for i in range(2, N-2):
        li = []
        for idx in [-2, -1, 1, 2]:
            li.append((H[i]-H[i+idx]))
        if min(li) > 0:
            count += min(li)
    return count


T = 10
for tc in range(1, T + 1):
    N = int(input())
    H = list(map(int, input().split()))

    res = find(N, H)
    print("#%d %d" % (tc, res))