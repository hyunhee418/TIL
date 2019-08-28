import sys
sys.stdin = open('sample_input_A2.txt', 'r')

T = int(input())

dx = [0, 0, -0.5, 0.5, 0]
dy = [0.5, -0.5, 0, 0, 0]

def isEnd(li):
    cnt = 0
    for i in range(len(li)):
        if li[i] != [0, 0, 4, 0]:
            cnt += 1
            if cnt == 1:
                return False
    if cnt == 0:
        return True

for tc in range(1, 1 + T):
    print("#%d" %(tc), end=' ')
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    s = 0
    result = 0
    while s <= 2000 and isEnd(li) == False:
        s += 0.5
        for i in range(len(li)):
            if li[i] == [0, 0, 4, 0]:
                pass
            else:
                li[i][0] = li[i][0] + dx[li[i][2]]
                li[i][1] = li[i][1] + dy[li[i][2]]
        for i in range(len(li)):
            same = []
            if li[i] == [0, 0, 4, 0]:
                pass
            for j in range(i+1, len(li)):
                if li[i] != li[j] and li[i] != [0, 0, 4, 0] and li[j] != [0, 0, 4, 0] and li[i][0] == li[j][0] and li[i][1] == li[j][1]:
                    if i not in same:
                        same.append(i)
                    if j not in same:
                        same.append(j)
            for idx in range(len(same)):
                result += li[same[idx]][3]
                li[same[idx]] = [0, 0, 4, 0]
    print(result)