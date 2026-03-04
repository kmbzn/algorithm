res = -1

A, B = map(int, input().split())
if A == B:
    res = 0
from collections import deque

Q = deque()

Q.append((A, 1))


while Q:
    popped = Q.popleft()
    pos = popped[0]
    dist = popped[1]
    if pos * 2 == B or pos * 10 + 1 == B:
        res = dist + 1
        break
    else:
        if pos * 2 < B:
            Q.append((pos * 2, dist + 1))
        if pos * 10 + 1 < B:
            Q.append((pos * 10 + 1, dist + 1))

print(res)