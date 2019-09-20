import sys
sys.stdin = open('sample_input_5207.txt', 'r')

def find(li, l, r, x):
    global result
    if 'll' not in result and 'rr' not in result:
        n = len(li)
        mid = (l+r)//2
        if li:
            if li[mid] == x:
                result += 'e'
                return
            elif li[mid] > x:
                result += 'r'
                find(li, l, mid-1, x)
            else:
                result += 'l'
                find(li, mid+1, r, x)


for tc in range(1, 1+int(input())):
    print('#%d' %(tc), end=' ')
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for b in B:
        result = ''
        if b in A:
            find(A, 0, N-1, b)
            if 'e' in result:
                cnt += 1
    print(cnt)