import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split(" "))
li = list(map(int, input().split(" ")))
count = 0
sum_v = 0
i = 0
j = 0
while i != N:
    sum_v += li[i]
    i += 1
    if sum_v == M:
        count += 1
        sum_v = 0
        j += 1
        i = j

    elif sum_v > M:
        sum_v = 0
        j += 1
        i = j
sum_v = 0
for i in range(j, len(li)):
    sum_v += li[i]
if sum_v == M:
    count += 1

print(count)
