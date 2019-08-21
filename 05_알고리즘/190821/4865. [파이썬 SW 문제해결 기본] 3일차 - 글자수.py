import sys
sys.stdin = open("sample_input_num_chr.txt", "r")

T = int(input())

for tc in range(1, T+1):
    print("#%d" %(tc), end=" ")
    str1 = str(input())
    str2 = str(input())
    max_cnt = 0
    cnt = 0
    for i in str1:
        for j in str2:
            if i == j:
                cnt += 1
        if cnt > max_cnt:
            max_cnt = cnt
        cnt = 0
    print(max_cnt)