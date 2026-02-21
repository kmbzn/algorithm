import sys
import collections

N = int(input())
L = list(map(int, sys.stdin.read().split()))
S = collections.deque()
S.append(0)

count = 0

res = ""

for i in L:
    if count < i:
        for j in range(i - count):
            res += "+\n"
            count += 1
            S.append(count)
        res += "-\n"
        S.pop()
    elif count > i and S[len(S) - 1] == i:
        res += "-\n"
        S.pop()
    else:
        res = "NO"
        break

print(res)