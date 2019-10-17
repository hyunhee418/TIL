import sys
sys.stdin = open('1436.txt', 'r')

N = int(input())
cnt = 0

for i in range(6660000):
    if '666' in str(i):
        cnt += 1
    if cnt == N:
        print(i)
        break

# 117856 KB 252 ms