import sys
sys.stdin = open("sample_input_bus.txt", "r")


def bus(K, M):
    bus_stop = [0] * (K[1] + 1)
    for i in M:
        bus_stop[i] += 1
    fuel = K[0]
    step = 0

    while fuel < K[1]:
        while bus_stop[fuel] != 1:
            fuel -= 1
            if fuel == 0:
                return 0
        bus_stop[fuel] += 1
        fuel += K[0]

    return bus_stop.count(2)

T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))
    H = list(map(int, input().split()))

    res = bus(N, H)
    print("#%d %d" % (tc, res))

