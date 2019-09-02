from collections import deque


li = deque([1, 5, 2, 4, 3])
rear, front = -1, -1
q = []
# def enQueue(a):
# #     rear = 0
# #     while rear < len(q):
# #         if q[rear] > a:
# #             break
# #         rear += 1
# #     q.insert(rear, a)
# #     return q
# #
# # def deQueue():
# #     global front
# #     front += 1
# #     q.pop(front)
# # for i in range(len(li)):
# #     enQueue(li[i])
# # print(q)

def enQueue(a):
    rear = 0
    extra_q = []
    while rear < len(q):
        if q[rear] > a:
            for _ in range(rear, len(q)):
                extra_q.append(deQueue())
        rear += 1
    q.append(a)
    q.extend(extra_q[::-1])
    return q

def deQueue():
    if q:
       return q.pop()

for i in range(len(li)):
    enQueue(li[i])
print(q)