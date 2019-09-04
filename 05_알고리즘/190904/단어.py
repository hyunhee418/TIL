import sys
sys.stdin = open('input_word.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    print('#%d' %(tc), end=' ')
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    re_cnt = 0
    flag = 0
    for i in range(N):
        flag = 0
        j = 0
        while j < N-K+1:
            if arr[i][j] == 1:
                for s in range(K):
                    if arr[i][j+s] == 1:
                        pass
                    else:
                        flag = 1
                        j = j+s-1
                        break
                if flag == 0:
                    if j+K == N:
                        re_cnt += 1
                        j = j + K - 1
                    else:
                        if arr[i][j+K] != 0:
                            s = 0
                            while j + K + s < N:
                                if arr[i][j+K+s] == 0:
                                    break
                                s += 1
                            j = j+K+s-1
                        else:
                            re_cnt += 1
                            j = j + K - 1
            j+= 1
            flag = 0

    for i in range(N):
        flag = 0
        j = 0
        while j < N-K+1:
            if arr[j][i] == 1:
                for s in range(K):
                    if arr[j+s][i] == 1:
                        pass
                    else:
                        flag = 1
                        j = j+s-1
                        break
                if flag == 0:
                    if j+K == N:
                        re_cnt += 1
                        j = j + K - 1
                    else:
                        if arr[j+K][i] != 0:
                            s = 0
                            while j + K + s < N:
                                if arr[j+K+s][i] == 0:
                                    break
                                s += 1
                            j = j+K+s-1
                        else:
                            re_cnt += 1
                            j = j + K - 1
            j+= 1
            flag = 0

    print(re_cnt)