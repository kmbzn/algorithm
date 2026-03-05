C, N = map(int, input().split())

DP = [float('inf')] * (C + 1)

DP[0] = 0

data = []

for _ in range(N):
    data.append(tuple(map(int, input().split())))

data.sort()

for price, get in data:
    for i in range(1, (C + 1)):
        if i - get < 0:
            if DP[i] > price:
                DP[i] = price
        else:
            if DP[i] > DP[i - get] + price:
                DP[i] = DP[i - get] + price

# print(data)

print(DP[-1])