def solution(N, number):
    answer = 0
    li = [0, [int(N)]]
    if N == number:
        return -1
    else:
        for i in range(2, 9):
            a = []
            a.append(int(str(N) * i))
            for j in range(1, i//2+1):
                for n in li[j]:
                    for y in li[i-j]:
                        if n+y not in a:
                            a.append(n+y)
                        if n-y not in a:
                            a.append(n-y)
                        if y-n not in a:
                            a.append(y-n)
                        if n * y not in a:
                            a.append(n * y)
                        if y !=0 and n != 0:
                            if n/y not in a:
                                a.append(int(n/y))
                            if y/n not in a:
                                a.append(int(y/n))

            if int(number) in a:
                return i
            li.append(a)
        return -1

print(solution(2,11))