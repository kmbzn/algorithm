import sys
N = int(sys.stdin.readline())

L = [0] * (N + 1)
L[0] = 1
L[1] = 1

for i in range(2, N + 1):
    L[i] = (L[i - 2] + L[i - 1]) % 15746

print(L[N])