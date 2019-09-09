import sys
sys.stdin = open('test.txt', 'r')
N = int(input())
input_li = list(map(int, input().split()))
arr = [[0, 0] for _ in range(N+1)]
for i in range(0, len(input_li)-1, 2):
    if not arr[input_li[i]][0]:
        arr[input_li[i]][0] = (input_li[i + 1])
    else:
        arr[input_li[i]][1] = (input_li[i + 1])
def func(x):
    print(x, end=' ')
    if arr[x][0]:
        func(arr[x][0])
    if arr[x][1]:
        func(arr[x][1])
func(1)
print()

def fu(x):
    if x:
        print(x, end=' ')
        fu(arr[x][0])
        fu(arr[x][1])
fu(1)
print()

arr2 = [[] for _ in range(N+1)]
for i in range(0, len(input_li)-1, 2):
    arr2[input_li[i]].append(input_li[i + 1])

def func2(x):
    print(x, end=' ')
    if arr2[x]:
        try:
            func2(arr2[x][0])
            func2(arr2[x][1])
        except IndexError:
            pass

func2(1)