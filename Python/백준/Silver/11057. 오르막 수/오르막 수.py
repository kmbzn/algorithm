N = int(input())

L = [[1 for j in range(10)] for i in range(N)]



for i in range(1, N):
    for j in range(0, 10):
        L[i][j] = sum(L[i - 1][0:j + 1]) % 10007


print(sum(L[N - 1]) % 10007)