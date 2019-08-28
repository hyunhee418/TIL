
def createQueue():
    return [0]*4

q = createQueue()
front = -1
rear = -1

def enQueue(a):
    global rear
    rear += 1
    q[rear] = a

def deQueue():
    global front
    front += 1
    return q[front]

def isEmpty():
    global rear
    global front
    if rear == front:
        return True
    else:
        return False

def isFull():
    global rear
    if rear == len(q)-1:
        return True
    else:
        return False

for i in range(1, 4):
    enQueue(i)
print(q)
for i in range(1, 4):
    print(deQueue())
print(isEmpty())

