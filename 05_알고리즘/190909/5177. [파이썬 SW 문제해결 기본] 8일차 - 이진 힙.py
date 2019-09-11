import sys
sys.stdin = open('sample_input (1).txt', 'r')

T = int(input())

# def tree_input(ele):
#     node = node2
#     node.append([])
#     li.append(ele)
#     node[li.index(ele)-1].append(ele)
#     if li[li.index(ele)-1] > ele:
#         node[li.index(ele)].append(li[li.index(ele)-1])
#         if node[li.index(ele)-1]:
#             if node[li.index(ele)-1][0] != ele:
#                 node[li.index(ele)].append(node[li.index(ele)-1][0])
#         for lit in range(len(node)):
#             if li[li.index(ele)-1] in node[lit]:
#                 node[lit].remove(li[li.index(ele)-1])
#                 node[lit].append(ele)
#                 break
#         node[li.index(ele)-1] = []

def ele_input(i):
    node[i] = input_li[i-1]
    n = 1
    while i//(2**n) != 0:
        x = i // 2 ** n
        if node[x] > node[i]:
            node[i],  node[x] = node[x], node[i]
            i = x
        else:
            n += 1


for tc in range(1, 1+T):
    print('#%d' %(tc), end=' ')
    N = int(input())
    input_li = list(map(int, input().split()))
    node = [0]*(N+1)
    sum_pa = 0
    for i in range(1, len(input_li)+1):
        ele_input(i)
    for n in range(1, i+1):
        if node[i//2**n] == 0:
            break
        sum_pa += node[i // 2 ** n]
    print(sum_pa)

    # for ele in range(1, len(input_li)):
    #     tree_input(input_li[ele])
    # print(node2)

# 처음에 노드하나 만들고
# 들어가는 순서에 맞춰 들어가고
# 부모노드와 크기를 비교한다