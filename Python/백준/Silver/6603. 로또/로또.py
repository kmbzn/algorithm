N = -1


def printList(l):
    res.append(l)

def select(l, s):
    if len(l) == 6:
        printList(l)
    else:
        for i in range(s - 1, len(l) - 8, -1):
            select(l[:i] + l[i + 1:], i)
    
while N != 0:
    res = []
    S = list(map(int, input().split()))
    N = S[0]
    select(S[1:], len(S) - 1)
    res.sort()
    for i in range(0, len(res)) :
        for j in range(0, 6) :
            print(res[i][j], end = " ")
        print()
    print()