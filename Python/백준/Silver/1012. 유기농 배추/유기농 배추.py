import sys
sys.setrecursionlimit(10 ** 9)

T = int(sys.stdin.readline())

for _ in range(T):


    res = 0
    M, N, K = map(int, sys.stdin.readline().split())
    L = [[0 for i in range(M)] for j in range(N)]
    def chk(X, Y):
        if L[Y][X] == 1:
            L[Y][X] = 0
        else:
            return
        
        if X != 0:
            chk(X - 1, Y)
        if X != len(L[0]) - 1:
            chk(X + 1, Y)
        if Y != 0:
            chk(X, Y - 1)
        if Y != len(L) - 1:
            chk(X, Y + 1)

    for i in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        L[Y][X] = 1
    
    for i in range(N):
        for j in range(M):
            if L[i][j] == 1:
                chk(j, i)
                res += 1
    print(res)
