from sys import stdin
from collections import deque

N = int(input())

visited = set()

parents = [0] * (N + 1)

L = [[] for i in range(N + 1)]

I = stdin.read().splitlines()

for i in I:
    a, b = map(int, i.split())
    L[a].append(b)
    L[b].append(a)

Q = deque()

Q.append(1)

while Q:
    popped = Q.popleft()

    for i in L[popped]:
        if i not in visited:
            visited.add(i)
            Q.append(i)
            parents[i] = popped


res = ''
for i in range(2, N + 1):
    res += str(parents[i]) + '\n'

print(res)
