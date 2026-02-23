import sys

N = int(sys.stdin.readline())

res = [[0, 0, 0]]

for i in range(N):
    res.append(list(map(int, sys.stdin.readline().split())))
    for j in range(3):
        res[i + 1][j] += min(res[i][(j + 1) % 3], res[i][(j + 2) % 3])

print(min(res[N]))