import sys
sys.stdin = open("input.txt", "r")

H, L = map(int, input().split(" "))
li = list(map(int, input().split(" ")))
max_i = li.index(max(li))
max_v = max(li)
result = 0
i = max_i
while i != 0 and max_i != 0:
    while i != 0 and li[i] >= li[i-1]:
        i -= 1
    while i != 0 and li[i] <= li[i-1]:
        i -= 1
    v = li[i]
    if li[i] != 0:
        for idx in range(i, max_i):
            if li[idx] < v:
                result += v-li[idx]
    max_v = li[idx]
    max_i = i
    i -= 1
max_i = li.index(max(li))
max_v = max(li)
i = max_i
while i != L-1 and max_i != L-1:
    while i != L-1 and li[i] >= li[i+1]:
        i += 1
    while i != L-1 and li[i] <= li[i+1]:
        i += 1
    if li[i] != 0:
        v = li[i]
        for idx in range(max_i+1, i):
            if li[idx] < v:
                result += v-li[idx]
    max_v = li[idx]
    max_i = i
    i += 1
print(result)