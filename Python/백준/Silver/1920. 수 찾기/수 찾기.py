import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

A.sort()

M = int(sys.stdin.readline())

B = list(map(int, sys.stdin.readline().split()))

res = ""

def find(start, end, item):
    if end - start == 1:
        if A[start] == item: return 1
        else: return 0;

    mid = (start + end + 1) // 2
    if item < A[mid]:
        return find(start, mid, item)
    else:
        return find(mid, end, item)

for i in B:
    res += str(find(0, N, i)) + "\n"

print(res)