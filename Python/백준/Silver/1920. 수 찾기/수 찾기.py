import sys

N = int(sys.stdin.readline())

A = set(map(int, sys.stdin.readline().split()))


M = int(sys.stdin.readline())

B = list(map(int, sys.stdin.readline().split()))

res = ""

for i in B:
    res += str(int(i in A)) + "\n"

print(res)