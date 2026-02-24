import sys
n, k = map(int, sys.stdin.readline().split())
coins = list(map(int, sys.stdin.read().splitlines()))
coins.sort()
DP = [0] * (k + 1)
DP[0] = 1
for coin in coins:
    for j in range(coin, k + 1):
        DP[j] += DP[j - coin]
print(DP[k])