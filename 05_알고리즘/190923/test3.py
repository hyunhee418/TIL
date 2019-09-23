import sys
sys.stdin = open('test3.txt', 'r')

def find(point, iidx):
    visited[iidx] = 1
    can = []
    for idx in range(10):
        if li[idx][0] == point and li[idx][1] in candidate and l[candidate.index(li[idx][1])] > li[idx][2] + l[iidx] and visited[candidate.index(li[idx][1])] == 0:
            l[candidate.index(li[idx][1])] = li[idx][2] + l[iidx]
            can.append(li[idx][1])
    min_re = 10000000000000
    for c in can:
        if min_re > l[candidate.index(c)]:
            min_re = l[candidate.index(c)]
    find(candidate[l.index(min_re)], l.index(min_re))


li = [[0, 0, 0] for _ in range(10)]
l = [0] + [1000000000]*5
visited = [0] * 6
candidate = []
for i in range(10):
    laa = list(input().split())
    li[i][0], li[i][1], li[i][2] = laa[0], laa[1], int(laa[2])

for x in range(10):
    if li[x][0] not in candidate:
        candidate.append(li[x][0])
    if li[x][1] not in candidate:
        candidate.append(li[x][1])
print(candidate)
find('a', 0)
print(l[-1])

