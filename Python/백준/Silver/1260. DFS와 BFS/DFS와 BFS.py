# 1260.py

# 정점의 개수는 최대 1000개

import sys, collections

N, M, V = map(int, input().split())

L = [[0 for i in range(N + 1)] for j in range(N + 1)]



visited = set()

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    L[a][b] = 1
    L[b][a] = 1


# 일단 그래프 세팅 완료했고

# BFS는 큐, DFS는 스택을 사용하지 아마.

# DFS

def DFS(n):
    if n in visited:
        return
    
    print(n, end = " ")
    visited.add(n)

    for i in range(1, N + 1):
        if L[n][i] and i not in visited:
            DFS(i)

DFS(V)

print()


# BFS


visited = set()
visited.add(V)

Q = collections.deque()
Q.appendleft(V)

while 1:
    if len(Q) == 0:
        break
    popped = Q.pop()
    print(popped, end = " ")
    
    for i in range(1, N + 1):
        if L[popped][i] and i not in visited:
            Q.appendleft(i)
            visited.add(i)