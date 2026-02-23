N = int(input())

L = [[1 for j in range(10)] for i in range(N)]

L[0][0] = 0


for i in range(1, N):
    L[i][0] = L[i - 1][1] % 1000000000
    L[i][9] = L[i - 1][8] % 1000000000
    for j in range(1, 9):
        L[i][j] = (L[i - 1][j - 1] + L[i - 1][j + 1]) % 1000000000

print(sum(L[N - 1]) % 1000000000)