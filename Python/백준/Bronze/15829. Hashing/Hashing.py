N = int(input())
S = input()
res = 0

for i in range(0, N):
    res += (ord(S[i]) - ord('a') + 1) * pow(31, i, 1234567891)
    res %= 1234567891

print(res)