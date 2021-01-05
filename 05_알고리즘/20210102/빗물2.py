import sys
sys.stdin = open("input.txt", "r")

H, L =map(int, input().split(" "))
li = list(map(int, input().split(" ")))
result = 0
for i in range(1, L):
    v = li[i]
    lMax = max(li[:i])
    rMax = max(li[i:])
    if rMax > v and lMax > rMax:
        result += rMax - v
    elif lMax > v and lMax <= rMax:
        result += lMax - v
print(result)