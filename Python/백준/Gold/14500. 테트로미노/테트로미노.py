import sys
N, M = map(int, input().split())
L = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()]

offset = [ [ 1, 1, 1, 1, 0, 0 ], [ 0, 0, 1, 1, 1, 1 ], [ 1, 1, 1, 0, 1, 0 ], [ 1, 1, 0, 1, 0, 1 ], [ 1, 0, 1, 0, 1, 1 ], [ 0, 1, 0, 1, 1, 1 ], [ 0, 1, 1, 1, 0, 1 ], [ 1, 0, 1, 1, 1, 0 ], [ 0, 1, 1, 1, 1, 0 ], [ 1, 0, 1, 1, 0, 1 ] ]

res = 0

for i in range(N):
    for j in range(M - 3):
        if sum(L[i][j:j+4]) > res:
            res = sum(L[i][j:j+4])

for i in range(N - 3):
    for j in range(M):
        s = sum(row[j] for row in L[i:i+4])
        if s > res:
            res = s

for i in range(N - 1):
    for j in range(M - 2):
        for o in offset:
            s = sum(L[i + dx % 2][j + dx // 2] * o[dx] for dx in range(0, 6))
            if s > res:
                res = s

for i in range(N - 2):
    for j in range(M - 1):
        for o in offset:
            s = sum(L[i + dx // 2][j + dx % 2] * o[dx] for dx in range(0, 6))
            if s > res:
                res = s




print(res)