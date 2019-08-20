stack = []

for i in range(2):  #push
    stack[top + 1] = i
    top += 1









def push(stack, a):
    stack.append(a)

def pop(stack):
    if len(stack):
        stack.pop(len(stack)-1)
    else:
        return

def isEmpty(stack):
    return bool(len(stack))

def peek(stack):
    if len(stack):
        return stack[len(stack)-1]
    else:
        return -1