N, K = map(int, input().split())

List = list(range(1, N + 1))

pos = K - 1
print("<", end = "")
while len(List) > 1:
    if pos >= len(List):
        pos %= len(List)
    print(List.pop(pos), end = ', ')
    pos += (K - 1)

print(List.pop(), end = '')
print(">", end = "")