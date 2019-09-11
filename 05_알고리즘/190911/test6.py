n = '01D06079861D79F99F'
# n = '0F97A3'

def Bbit_print(i):
    global re
    output = ''
    for j in range(3, -1, -1):
        output += '1' if i & (1<<j) else '0'
    re += output
re = ''
for i in n:
    if ord(i)-ord('A') >= 0:
        Bbit_print(ord(i)-ord('A')+10)
    else:
        Bbit_print(int(i))

li = list(map(int, re))

result = [0]*(len(li)//7+1)
for i in range(0, len(li), 7):
    sum_re = 0
    if i + 6 < len(li):
        for j in range(7):
            if li[i+j]:
                sum_re += 2**(6-j)
    else:
        for j in range((len(li) - i)-1, -1, -1):
            if li[i + j]:
                sum_re += 2**(j)
    result[i//7] = sum_re


if len(li) % 7:
    print(' '.join(list(map(str, result))))
else:
    print(' '.join(list(map(str, result[:len(li)-1]))))