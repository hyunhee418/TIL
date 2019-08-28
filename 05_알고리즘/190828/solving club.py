import sys
sys.stdin = open('sample_input.txt', 'r')

def cardgame(string):
    li = [13]*4
    cards = []
    for i in range(len(string)):
        if string[i] == 'S':
            if ('S',int(string[i+1:i+3])) not in cards:
                cards.append(('S',int(string[i+1:i+3])))
                li[0] -= 1
            else:
                return  'ERROR'

        if string[i] == 'D':
            if ('D',int(string[i+1:i+3])) not in cards:
                cards.append(('D',int(string[i+1:i+3])))
                li[1] -= 1
            else:
                return  'ERROR'


        if string[i] == 'H':
            if ('H',int(string[i+1:i+3])) not in cards:
                cards.append(('H',int(string[i+1:i+3])))
                li[2] -= 1
            else:
                return  'ERROR'

        if string[i] == 'C':
            if ('C',int(string[i+1:i+3])) not in cards:
                cards.append(('C',int(string[i+1:i+3])))
                li[3] -= 1
            else:
                return  'ERROR'
    result = ' '.join(list(map(str, li)))
    return result

T = int(input())

for tc in range(1, 1+T):
    print("#%d" %(tc), end=" ")
    string = str(input())
    print(cardgame(string))