import sys, collections
sys.stdin = open("input.txt", "r")
li = []
q = collections.deque()
while True:
    try:
        li.append(int(input()))
    except:
        break
visited = [0]*len(li)
i = 1
d = 0
q.append(li[0])
while q:
    if i+1 >= len(li):

        print(li[-1])
        while q:
            print(q.pop())
        break
    else:
        if (d ==0 and li[i] < li[i+1]):
            if q[-1] < li[i + 1]:
                print(li[i])
            else:
                q.append(li[i])
            d = 1
        elif d==1 and li[i] < li[i+1]:
            if q[-1] < li[i+1]:
                print(li[i])
                print(q.pop())
            else:
                q.append(li[i])
        elif d==1 and li[i] >= li[i+1]:
            d=0
            q.append(li[i])
        else:
            q.append(li[i])
        i+=1