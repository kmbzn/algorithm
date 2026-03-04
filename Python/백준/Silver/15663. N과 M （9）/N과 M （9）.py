from itertools import permutations

N, M = map(int, input().split())

L = list(map(int, input().split()))

L.sort()

C = permutations(L, M)

S = set()

L = []

for i in C:
    if i not in S:
        L.append(i)
        S.add(i)

L.sort()

for i in L:
    l = list(i)
    for j in l:
        print(j, end = ' ')
    print()
