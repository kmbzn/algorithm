from sys import stdin
from collections import deque

M, N, K = map(int, input().split())

L = [[1 for j in range(M)] for i in range(N)]

readed = stdin.read().splitlines()

for _ in readed:
    sj, si, ej, ei = map(int, _.split())
    for i in range(si, ei):
        for j in range(sj, ej):
            L[j][i] = 0

offset = [ [ -1, 0 ], [ 1, 0 ], [ 0, -1 ], [ 0, 1 ] ]

res = 0

# for i in L:
#     for j in i:
#         print(j, end = ' ')
#     print()

resArea = []

for i in range(N):
    for j in range(M):
        if L[i][j] == 1:
            Q = deque()
            Q.append([i, j])
            L[i][j] = 0
            res += 1
            area = 1
            while Q:
                popped = Q.pop()
                pi = popped[0]
                pj = popped[1]
                for d in offset:
                    di = d[0]
                    dj = d[1]
                    if 0 <= pi + di < N and 0 <= pj + dj < M and L[pi + di][pj + dj]:
                        L[pi + di][pj + dj] = 0
                        Q.append([pi + di, pj + dj])
                        area += 1
            resArea.append(area)


resArea.sort()
print(res)
for i in resArea:
    print(i, end = ' ')