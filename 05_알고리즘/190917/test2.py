import sys
sys.stdin = open('test2.txt', 'r')

def func1(k, li):
    global result, f
    result1 = result
    if k == len(li):
        for i in range(k):
            result1.append(li[i])
        if (li[0] == li[1] == li[2] or li[0] == li[1] +1 == li[2] + 2) and (li[3] == li[4]+1 == li[5]+2 or li[3] == li[4] == li[5]):
            result.append('babygin!')
            return
    else:
        for j in range(k, len(li)):
            li[k], li[j] = li[j], li[k]
            func1(k+1, li)
            li[k], li[j] = li[j], li[k]

for tc in range(1, 6):
    print('#%d' %(tc), end=' ')
    li = list(map(int, input()))
    result = []
    func1(0, li)
    if 'babygin!' in result:
        print('babygin!')
    else:
        print('fail')