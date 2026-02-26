N, K = map(int, input().split())

L = [[] for _ in range(N)]

for i in range(N):
    l = list(map(int, input().split()))
    L[l[0] - 1] = l[1:]

target = L[K - 1]

L.sort(reverse=True)


for ans in range(N):
    if L[ans] == target:
        print(ans + 1)
        break