import sys
sys.stdin = open("input_divset.txt", "r")

initial_li = [number for number in range(1, 13)]

def sum_h(a):
    sum_v = 0
    for i in a:
        sum_v += i
    return sum_v



T = int(input())
for tc in range(1, T+1):
    count = 0
    a, b = map(int, input().split())
    for i in range(1, 1 << len(initial_li)):
        li = [initial_li[j] for j in range(len(initial_li)) if i & (1 << j)]
        if len(li) == a and sum_h(li) == b:
            count += 1

    print("#%d %d" %(tc, count))