import sys
sys.stdin = open('sample_input_5204.txt', 'r')

def merge(left, right):
    global cnt
    i, k, j = 0, 0, 0
    result = [0]*(len(left) + len(right))
    if left[-1] > right[-1]:
        cnt += 1
    while i < len(result):
        if k < len(left) and j < len(right):
            if left[k] <= right[j]:
                result[i] = left[k]
                i += 1
                k += 1
            else:
                result[i] = right[j]
                i += 1
                j += 1
        elif k < len(left):
            result[i] = left[k]
            i += 1
            k += 1
        elif j < len(right):
            result[i] = right[j]
            i += 1
            j += 1
    return result

def merge_sort(li):
    global N
    if len(li) == 1:
        return li
    middle = len(li) // 2
    left = li[:middle]
    right = li[middle:N]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


for tc in range(1, 1+int(input())):
    print('#%d' %(tc),end=' ')
    N = int(input())
    li = list(map(int, input().split()))
    cnt = 0
    print(merge_sort(li)[N//2], cnt)