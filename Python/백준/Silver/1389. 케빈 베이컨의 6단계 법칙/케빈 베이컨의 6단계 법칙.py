import collections

N, M = map(int, input().split())

L = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    L[a].append(b)
    L[b].append(a)

bacon = [0] * (N + 1)



for a in range(1, N + 1):
    Q = collections.deque()
    dist = [-1] * (N + 1)
    Q.append(a)
    dist[0] = 0
    dist[a] = 0
    for _ in range(N):
        if len(Q):
            popped = Q.popleft()
        for i in L[popped]:
            if dist[i] == -1:
                Q.append(i)
                dist[i] = dist[popped] + 1

    bacon[a] = sum(dist[1:])

min = bacon[1]
res = 1

for i in range(1, N + 1):
    if min > bacon[i]:
        res = i
        min = bacon[i]

print(res)