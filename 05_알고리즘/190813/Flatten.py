import sys
sys.stdin = open("input (1).txt", "r")

def flatten(move, heights):

    for _ in range(move):
        max_value = heights[0]
        min_value = heights[0]
        for height in heights[1:]:
            if height > max_value:
                max_value = height
            elif height < min_value:
                min_value = height
        max_idx = heights.index(max_value)
        min_idx = heights.index(min_value)
        heights.pop(max_idx) and heights.insert(max_idx, max_value - 1)
        heights.pop(min_idx) and heights.insert(min_idx, min_value + 1)
    max_v = heights[0]
    min_v = heights[0]
    for ele in heights[1:]:
        if ele > max_v:
            max_v = ele
        elif ele < min_v:
            min_v = ele
    return max_v - min_v

for tc in range(10):
    N = int(input())
    H = list(map(int, input().split()))
    res = flatten(N, H)

    print("#%d %d" %(tc, res))