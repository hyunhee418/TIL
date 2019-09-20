import sys
sys.stdin = open('sample_input_5205.txt', 'r')


def sort_h(l, r):
    mid = l
    l_s = 0
    r_s = 0
    if l < r:
        while l+l_s < r+r_s:
            while arr[mid] >= arr[l+l_s] and l+l_s < r:
                l_s += 1
            while arr[mid] <= arr[r+r_s] and r+r_s > l:
                r_s -= 1
            if l+l_s < r+r_s:
                arr[l+l_s], arr[r+r_s] = arr[r+r_s], arr[l+l_s]
        arr[mid], arr[r+r_s] = arr[r+r_s], arr[mid]
        sort_h(l, r+r_s-1)
        sort_h(r+r_s+1, r)



for tc in range(1, int(input())+1):
    print('#%d' %(tc), end=' ')
    N = int(input())
    arr = list(map(int, input().split()))
    sort_h(0, N-1)
    print(arr[N//2])