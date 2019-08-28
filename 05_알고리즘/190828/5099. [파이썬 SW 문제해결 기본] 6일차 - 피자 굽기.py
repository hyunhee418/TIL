import sys
sys.stdin = open('sample_input_5099.txt', 'r')

q = [0]*200
rear, front = -1, -1
li = []
i = 0


def cycle(j):
    for i in range(len(q), 0, -1):
        q[(i+1) % len(q)] = q[i]
        li[i] = i
    for i in range(len(q)):
        if i % len(q) == 0
            if q[i] == 0:
                li[i + j] == i
                q[i] = li[i]
            else:
                q




    # for i in range(N):
    #     rear = (j + i) % len(q)
    #     if rear % N == 0:
    #         if q[rear] != 0:
    #             li[i+j] == rear
    #             q[rear] = li[i+j]//2
    #         else:
    #             q[rear] = li[i]
    #             li[i+j] = 0



def deQueue():
    global front
    front = (front+1) % len(q)

def isRemainder(q):
    cnt = 0
    global i
    for s in range(len(q)):
        if q[s] != 0:
            cnt += 1
            if cnt == 2:
                return False
    if cnt == 1 and i == len(q)-1:
        for s in range(len(q)):
            if q[s] != 0:
                return s
    else:
        return False

def isZero(q, li):
    for i in range(len(q)):
        if q[i] == 0:
            q[i]


T = int(input())
for tc in range(1, T+1):
    print("#%d" %(tc), end=" ")
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    q = [0]* (2*N)
    rear, front = -1, -1
    s = N


    while not isRemainder(q):
        for j in range(N):
            cycle(j)



    print(isRemainder(q)+1)