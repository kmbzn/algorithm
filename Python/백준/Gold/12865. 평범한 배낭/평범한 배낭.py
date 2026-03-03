from sys import stdin

N, K = map(int, input().split())

L = [list(map(int, i.split())) for i in stdin.read().splitlines()]

L.sort()

bag = [0] * (K + 1)


for j in range(N):
    for i in range(K, 0, -1):
        weight = L[j][0]
        value = L[j][1]
        if weight <= i:
            if bag[i] < bag[i - weight] + value:
                bag[i] = bag[i - weight] + value

print(bag[-1])