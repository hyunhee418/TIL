import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

def inorder_traverse(T):
    global arr, l, i
    if T:
        inorder_traverse(arr[T][0])
        l[T] = i
        i += 1
        inorder_traverse(arr[T][1])

for tc in range(1, T+1):
    print('#%d' %(tc), end=' ')
    N = int(input())
    l = [0]*(N+1)

    arr = [[0, 0] for _ in range(N+1)]
    for i in range(2, N+1, 2):
        arr[i//2][0] = i
        if i+1 < N+1:
            arr[i//2][1] = i+1
    i = 1
    inorder_traverse(1)
    print(l[1], l[N//2])