import collections

N, K = map(int, input().split())

S = []

D = dict()

S.append(set())

D[N] = 0

Q = collections.deque()
Q.append(N)

while len(Q):
    tmp = Q.popleft()
    if tmp == K:
        print(D[tmp])
        break
    if 0 < tmp:
        if (tmp - 1) not in D.keys():
            Q.append(tmp - 1)
            D[tmp - 1] = D[tmp] + 1
    if tmp < K:
        if ((tmp + 1) not in D.keys()) and tmp < K:
                Q.append(tmp + 1)
                D[tmp + 1] = D[tmp] + 1
        if (tmp * 2) not in D.keys():
            Q.append(tmp * 2)
            D[tmp * 2] = D[tmp] + 1