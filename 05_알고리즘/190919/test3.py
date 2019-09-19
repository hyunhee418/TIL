import sys
sys.stdin = open('test3.txt', 'r')


def preorder_traverse(x):
    if x:
        print(x, end=' ')
        preorder_traverse(li[x][0])
        preorder_traverse(li[x][1])

def inorder_traverse(x):
    if x:
        inorder_traverse(li[x][0])
        print(x, end=' ')
        inorder_traverse(li[x][1])

def postorder_traverse(x):
    if x:
        postorder_traverse(li[x][0])
        postorder_traverse(li[x][1])
        print(x, end=' ')
N = int(input())
l = list(map(int, input().split()))
li = [[0, 0] for _ in range(max(l)+1)]
for i in range(0, len(l)-1, 2):
    if li[l[i]][0]:
        li[l[i]][1] = l[i+1]
    else:
        li[l[i]][0] = l[i+1]
print(li)
preorder_traverse(1)
print()
inorder_traverse(1)
print()
postorder_traverse(1)