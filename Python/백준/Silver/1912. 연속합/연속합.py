N = int(input())

L = list(map(int, input().split()))

for i in range(1, N):
    L[i] += L[i - 1]

m = 0
M = L[0]

for i in L:
    if i - m > M:
        M = i - m
    if i < m:
        m = i
    
print(M)