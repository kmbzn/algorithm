import sys

N = int(input())

L = [list(map(int, i.split())) for i in sys.stdin.read().splitlines()]

for i in range(N):
    for j in range(i + 1):
        tmp = [0]
        if j < i:
            tmp.append(L[i-1][j])
        if 0 < j:
            tmp.append(L[i-1][j-1])
        L[i][j] += max(tmp)

print(max(L[N - 1]))