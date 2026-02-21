import sys

L = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]

for i in range(21):
    for j in range(21):
        L[i][j][0] = 1
        L[j][0][i] = 1
        L[0][i][j] = 1


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    if L[a][b][c] != 0:
        return L[a][b][c]

    if a < b and b < c:
        L[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return L[a][b][c]
    L[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return L[a][b][c]

A, B, C = map(int, sys.stdin.readline().split())
while A != -1 or B != -1 or C != -1:
    print("w(" + str(A) + ", " + str(B) + ", " + str(C) + ") = " + str(w(A, B, C)))
    A, B, C = map(int, sys.stdin.readline().split())