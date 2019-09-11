import sys
sys.stdin = open('input.txt', 'r')



def cal(i, b, a):
    if i == '+':
        return a + b
    elif i == '-':
        return a - b
    elif i == '*':
        return a * b
    elif i == '/':
        return a / b


def traverse(T):
    if T:
        traverse(tree[T][0])
        traverse(tree[T][1])
        c = tree[T][2]
        if type(c) == int:
            candidates.append(tree[T][2])
        else:
            cc = cal(c, candidates.pop(-1), candidates.pop(-1))
            candidates.append(cc)


for tc in range(1, 11):
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N + 1)]

    for i in range(N):
        put = input().split()
        parent = int(put[0])

        if len(put) == 4:
            tree[parent][0] = int(put[2])
            tree[parent][1] = int(put[3])
            tree[parent][2] = put[1]
        else:
            tree[parent][2] = int(put[1])

    candidates = []
    traverse(1)
    print('#%d %.d' % (tc, candidates[0]))