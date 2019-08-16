import sys
sys.stdin = open("sample_input_sum.txt", "r")

def div_sum(N, numbers):
    max_num = min_num = sum_num = 0
    for i in range(int(N[1])):
        sum_num += numbers[i]
        max_num = min_num = sum_num
    for idx in range(int(N[1]), len(numbers)):
        sums = sum_num - numbers[idx-int(N[1])] + numbers[idx]
        if sums > max_num:
            max_num = sum_num = sums
        elif sums < min_num:
            min_num = sum_num = sums
        else:
            sum_num = sums
    return max_num - min_num


T = int(input())
for tc in range(1, T+1):
    H = list(map(int,input().split()))
    N = list(map(int,input().split()))
    res = div_sum(H, N)

    print("#%d %d" %(tc, res))
