
q = [0] * 100
rear = -1
front = -1
myjju = 20
v = [0] * 100
i = 2

def enQueue(a):
    global rear, myjju
    rear = +1
    q[rear] = a
    v[a] += 1
    myjju -= v[a]

def deQueue():
    global front
    front = + 1

while myjju > 0:
    for j in range(1, i):
        enQueue(j)
        deQueue()
    i += 1
print(j)