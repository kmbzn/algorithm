import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())

adj = [[] for _ in range(N + 1)]

v = [1]

def top2(L):
    if len(L) <= 2:
        return L
    maxidx = 0
    mx = 0
    for i in range(len(L)):
        if L[i] > mx:
            maxidx = i
            mx = L[i]
    return [mx, max(L[:maxidx] + L[maxidx + 1:])]

import sys

for line in sys.stdin.read().splitlines():
    i, j, k = map(int, line.split())
    adj[i].append([j, k])
    adj[j].append([i, k])

res = 0

def build(n):
    global res
    
    child = []
    
    for nxt in adj[n]:
        if nxt[0] not in v:
            v.append(nxt[0])
            child.append(max(build(nxt[0])) + nxt[1])
    if len(child) == 0:
        return [0]
    if res < sum(top2(child)) :
        res = sum(top2(child))
    return top2(child)


build(1)
print(res)