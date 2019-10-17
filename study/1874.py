import sys
sys.stdin = open('1874.txt', 'r')

N = int(input())

li = [int(input()) for _ in range(N)]
l = sorted(li)
stack = [0, l[0]]
result = ['+']
i = 0
idx = 0
while i < N and idx < N+1:
    while idx < N+1 and i < N:
        if stack[-1] == li[i]:
            i += 1
            stack.pop(-1)
            result.append('-')
        else:
            idx += 1
            if idx >= N:
                break
            stack.append(l[idx])
            result.append('+')

if len(stack) > 1:
    print('NO')
else:
    for i in range(len(result)):
        print(result[i])