import sys
sys.stdin = open('2231.txt', 'r')

N = int(input())
re = 0
K = 0
f = 0
while K <= N:
    k_ele = 0
    for k in str(K):
        k_ele += int(k)
    if K+k_ele == N:
        f = 1
        print(K)
        break
    else:
        K += 1

if f == 0:
    print(0)

    # 117592 KB 460 ms