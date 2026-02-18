def select(res, idx):
    if len(res) == 6:
        for i in res:
            print(i, end = ' ')
        print()
    elif idx < len(S):
        select(res + [S[idx]], idx + 1)
        select(res, idx + 1)
    
while True:
    S = list(map(int, input().split()))
    N = S[0]
    if N == 0:
        break
    S = S[1:]
    select([], 0)
    print()