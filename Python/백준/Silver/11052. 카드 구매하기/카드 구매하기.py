import sys

sys.setrecursionlimit(10 ** 9)

N = int(input())

P = list(map(int, input().split()))
P = [0] + P
L = [0 for _ in range(0, N + 1)]

L[1] = P[1]
def f(n):
    if n == 0:
        return 0
    if L[n] != 0: # 있으면
        return L[n]
    
    maxRes = P[n]
    for i in range(1, n):
        if maxRes < f(i) * (n // i) + f(n % i):
            maxRes = f(i) * (n // i) + f(n % i)

    L[n] = maxRes
    return L[n]
    
print(f(N))