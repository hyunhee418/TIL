import sys
sys.stdin = open("sample_input.txt", "r")

def minmax(data):
    min_num = 1000000
    max_num = 0
    for idx in range(len(data)):
        if data[idx] > max_num:
            max_num = data[idx]
        if data[idx] < min_num:
            min_num = data[idx]
    return max_num - min_num
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = list(map(int, input().split()))

    res = minmax(H)
    print("#%d %d" % (tc, res) )
