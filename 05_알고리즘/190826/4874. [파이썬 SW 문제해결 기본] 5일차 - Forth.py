import sys
sys.stdin = open('sample_input_4874.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    print("#%d" %(tc), end=" ")
    li = list(map(str, input().split()))
    stack = []
    cal = ['+', '-', '*', '/']


    for num in range(len(li)):
        if li[num] not in cal and li[num] != '.':
            stack.append(int(li[num]))
        elif li[num] == '+':
            if len(stack) < 2:
                print("error")
                break
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)

        elif li[num] == '-':
            if len(stack) < 2:
                print("error")
                break
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)

        elif li[num] == '/':
            if len(stack) < 2:
                print("error")
                break
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(b // a)

        elif li[num] == '*':
            if len(stack) < 2:
                print("error")
                break
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)

        if li[num] == '.':
            if len(stack) != 1:
                print("error")
            else:
                print(int(stack.pop()))
