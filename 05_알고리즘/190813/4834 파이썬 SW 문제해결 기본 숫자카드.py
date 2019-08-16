import sys
sys.stdin = open("sample_input_card.txt", "r")

def card_game(cards):
    dict_card = {}
    max_value = 0
    li = []
    max_k = 0
    for card in list(cards):
        dict_card[card] = 0
    for card in list(cards):
        dict_card[card] += 1
    for dict_value in dict_card.values():
        if dict_value > max_value:
            max_value = dict_value
    for k, v in dict_card.items():
        if v == max_value:
            li.append(int(k))
    if len(li) != 1:
        for k in li:
            if k > max_k:
                max_k = k
    else:
        max_k = li[0]
    return max_k, max_value

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    H = str(input())
    res = card_game(H)
    res_1 = res[0]
    res_2 = res[1]
    print("#%d %d %d" %(tc, res_1, res_2))