import sys
sys.stdin = open("input_find.txt", "r")


def find(p, key):
    start = 1
    count = 1
    middle = int((start + p) / 2)
    while middle != key:
        if middle > key:
            p = middle
            count += 1
        else:
            start = middle
            count += 1
        middle = int((start + p) / 2)
    return count

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    if find(P, A)  > find(P, B):
        print("#%d B" %(tc))
    elif find(P, A)  < find(P, B):
        print("#%d A" %(tc))
    else:
        print("#%d 0" %(tc))

