# 9663. N-Queen

N = int(input())

v = [True] * N
v2 = [True] * (2 * N - 1)
v3 = [True] * (2 * N - 1)

def Queen(y):
    if y == N:
        return 1
    res = 0
    for i in range(N):
        if v[i] and v2[y + i] and v3[y - i + N - 1]:
            v[i] = v2[y + i] = v3[y - i + N - 1] = False
            res += Queen(y + 1)
            v[i] = v2[y + i] = v3[y - i + N - 1] = True
    return res

print(Queen(0))