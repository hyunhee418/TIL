import sys
sys.stdin = open('sample_input_5097.txt', 'r')

q = [0] * 10000
rear, front = -1, -1

def enQueue(a):
    global rear
    rear += 1
    q[rear] = a

def deQueue():
    global front
    front += 1

T = int(input())
for tc in range(1, 1+T):
    print('#%d'%(tc), end=' ')
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    q = [0] * 10000
    rear, front = -1, -1

    for i in range(len(li)):
        enQueue(li[i])

    for _ in range(M):
        deQueue()
        enQueue(q[front])

    print(q[front+1])
