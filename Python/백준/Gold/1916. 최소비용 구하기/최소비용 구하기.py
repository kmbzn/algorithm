from collections import deque

import heapq
from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())

D = [[] for _ in range(N + 1)]

INPUT = stdin.read().splitlines()

for i in range(M):
    a, b, c = map(int, INPUT[i].split())
    heapq.heappush(D[a], (c, b))

s, e = map(int, INPUT[M].split())

visited = [float('inf')] * (N + 1)

Q = [(0, s)]
visited[s] = 0

while Q:
    to, p = heapq.heappop(Q)
    for j in D[p]:
        if visited[j[1]] > to + j[0]:
            visited[j[1]] = to + j[0]
            if j[1] != e:
                heapq.heappush(Q, (to + j[0], j[1]))

print(visited[e])