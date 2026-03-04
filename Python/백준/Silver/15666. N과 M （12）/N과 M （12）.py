from itertools import combinations_with_replacement

N, M = map(int, input().split())

L = list(map(int, input().split()))

L.sort()

C = combinations_with_replacement(L, M)

S = set()

L = []

for i in C:
    if i not in S:
        L.append(i)
        S.add(i)

L.sort()

for i in L:
    l = list(i)
    l.sort()
    for j in l:
        print(j, end = ' ')
    print()
