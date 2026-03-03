from itertools import combinations

N, M = map(int, input().split())

L = list(map(int, input().split()))

L.sort()

for i in combinations(L, M):
    for j in i:
        print(j, end = ' ')
    print()