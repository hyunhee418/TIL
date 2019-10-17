import sys
sys.stdin = open('2164.txt', 'r')
import collections

l = collections.deque([num for num in range(1, 1+int(input()))])

while len(l) > 1:
    l.popleft()
    l.append(l.popleft())
print(l[0])