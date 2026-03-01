from itertools import combinations
from sys import stdin
N = int(input())
L = [list(map(int, i.split())) for i in stdin.read().splitlines()]
item = range(1, N)

c = combinations(item, N // 2 - 1)

all = set(range(N))

min = float('inf')

for l in c:
    l = [0] + list(l)
    p1 = p2 = 0
    d = all - set(l)
    for i in l:
        for j in l:
            p1 += L[i][j]
    for i in d:
        for j in d:
            p2 += L[i][j]
    if min > abs(p1 - p2):
        min = abs(p1 - p2)

print(min)
