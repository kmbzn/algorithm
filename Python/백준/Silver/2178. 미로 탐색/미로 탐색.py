from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

L = [[0 for j in range(M)] for i in range(N)]

s = sys.stdin.read().splitlines()

for i in range(N):
    for j in range(M):
        if int(s[i][j]):
            L[i][j] = 1

Q = deque()
Q.append([0, 0, 1])

while Q:
    popped = Q.popleft()
    i, j, k = popped[0], popped[1], popped[2]


    di = [ -1, 1, 0, 0 ]
    dj = [ 0, 0, -1, 1 ]

    brk = 0

    for _ in range(4):
        if 0 <= i + di[_] < N and 0 <= j + dj[_] < M and L[i + di[_]][j + dj[_]]:
            if i + di[_] == N - 1 and j + dj[_] == M - 1:
                print(k + 1)
                brk = 1
                break
            L[i + di[_]][j + dj[_]] = 0
            Q.append([i + di[_], j + dj[_], k + 1])
    if brk:
        break