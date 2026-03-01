import math
from collections import deque

res = 0

F, S, G, U, D = map(int, input().split())

if not U:
    if not D:
        res = -1
    elif S < G:
        res = -1
    elif S > G:
        if (S - G) % D:
            res = -1
        else:
            res = (S - G) // D
elif not D:
    if G < S:
        res = -1
    elif S < G:
        if (G - S) % U:
            res = -1
        else:
            res = (G - S) // U
elif S == G:
    res = 0
elif abs(G - S) % math.gcd(U, D):
    res = -1
else:
    Q = deque([S])
    while Q:
        popped = Q.popleft()
        if G > popped:
            if popped + U <= F:
                Q.append(popped + U)
            elif popped - D > 0:
                Q.append(popped - D)
            else:
                res = -1
                break
        elif G < popped:
            if popped - D > 0:
                Q.append(popped - D)
            elif popped + U <= F:
                Q.append(popped + U)
            else:
                res = -1
                break
        else:
            break
        res += 1

if res == -1:
    print("use the stairs")
else:
    print(res)