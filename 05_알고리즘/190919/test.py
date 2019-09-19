import sys
sys.stdin = open('test.txt', 'r')


def quickSort(l, r):
    li=li1
    min = l
    s = 0
    l_s = 0
    if l < r:
        while l+l_s < r+s:
            s = 0
            l_s = 0
            while li[min] >= li[l+l_s] and l+l_s < r:
                l_s += 1
            while li[min] <= li[r+s] and r+s > l:
                s -= 1
            if l+l_s < r+s:
                li[l+l_s], li[r+s] = li[r+s], li[l+l_s]

        li[min], li[r+s] = li[r+s], li[min]
        quickSort(l, r+s-1)
        quickSort(r+s+1, r)
T= int(input())
for tc in range(1, 1+T):
    print('#%d' %(tc), end=' ')
    li1 = list(map(int, input().split()))
    quickSort(0, len(li1)-1)
    print(li1)