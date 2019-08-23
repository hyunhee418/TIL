import sys
sys.stdin = open("sample_input_4873.txt", "r")

T = int(input())

for tc in range(1, T+1):
    print("#%d" %(tc), end=" ")
    li = [s for s in input()]
    stack = [1]
    for i in range(len(li)):
        if stack[-1] != li[i]:
            stack.append(li[i])
        else:
            stack.pop()

    print(len(stack)-1)