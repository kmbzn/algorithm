from sys import stdin

T = int(stdin.readline())

L = [0] * (1000001)
L[1], L[2], L[3] = 1, 2, 4

for i in range(4, 1000001):
    for j in range(1, 4):
        L[i] += L[i - j]
    L[i] %= 1000000009

for _ in range(T):
    N = int(stdin.readline())
    print(L[N])