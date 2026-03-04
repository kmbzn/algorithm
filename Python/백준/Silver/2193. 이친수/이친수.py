DP0, DP1 = 0, 1

N = int(input())

for _ in range(N - 1):
    DP0, DP1 = DP0 + DP1, DP0

print(DP0 + DP1)