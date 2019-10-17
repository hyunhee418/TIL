import sys
sys.stdin =open('d.txt', 'r')


s = input()
N = len(s)
num = [0]*N
cal = [0]*N
numlen = 0
minus = [0]*N
re = [0]*N
if '+' not in s and '-' not in s:
    print(int(s))
else:
    for i in range(N):
        if s[i] == '+':
            for num_i in range(len(num)):
                if num[num_i] == 0:
                    num[num_i] = int(s[numlen:i])
                    numlen = i+1
                    break
            for cal_i in range(len(cal)):
                if cal[cal_i] == 0:
                    cal[cal_i] = '+'
                    break
        elif s[i] == '-':
            for num_i in range(len(num)):
                if num[num_i] == 0:
                    num[num_i] = int(s[numlen:i])
                    numlen = i+1
                    minus[num_i] = 1
                    break
            for cal_i in range(len(cal)):
                if cal[cal_i] == 0:
                    cal[cal_i] = '-'
                    break
    f = 0
    for i in range(N-1, -1, -1):
        if s[i] == '-' or s[i] == '+':
            for num_i in range(len(num)):
                if num[num_i] == 0:
                    num[num_i] = int(s[i+1:N])
                    f = 1
                    break
        if f:
            break
    for i in range(len(minus)):
        if minus[i]:
            for ii in range(i+1, len(minus)):
                num[0] -= num[ii]
                if minus[ii]:
                    break
    print(num[0])
