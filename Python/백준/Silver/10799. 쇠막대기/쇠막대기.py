import sys

S = sys.stdin.readline().strip()

level = 0

laser = False

ans = 0

for i in S:
    if i == '(':
        level += 1
        laser = True
    elif i == ')':
        level -= 1
        if laser:
            ans += level
        else:
            ans += 1
        laser = False

print(ans)