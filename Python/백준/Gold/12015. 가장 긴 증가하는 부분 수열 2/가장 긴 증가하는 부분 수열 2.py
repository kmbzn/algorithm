from sys import stdin
from bisect import bisect_left

N = int(stdin.readline())
L = list(map(int, stdin.readline().split()))

arr = [L[0]]

for i in range(1, N):
    if L[i] > arr[-1]:
        arr.append(L[i])
    elif L[i] < arr[-1]:
        arr[bisect_left(arr, L[i])] = L[i]
    
print(len(arr))