import sys
sys.stdin = open('2303.txt', 'r')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
max_num = 0
max_idd = 0
t = [0]*3
def perm(k, idx):
    global max_card
    if k == 3:
        sum_card = sum(t)
        ss = str(sum_card)[-1]
        if int(ss) > max_card:
            max_card = int(ss)
    else:
        for i in range(5):
            if visited[i]:
                continue
            t[k] = arr[idx][i]
            visited[i] = 1
            perm(k+1, idx)
            visited[i] = 0
for idx in range(N):
    max_card = 0
    visited = [0]*5
    perm(0, idx)
    a = max_card
    if a >= max_num:
        max_num = a
        max_idd = idx

print(max_idd+1)