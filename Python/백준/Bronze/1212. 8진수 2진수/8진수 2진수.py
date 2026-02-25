a = input()

res = []

for i in a:
    eight = int(i)
    tmp = [0] * 3
    for j in range(3):
        tmp[2 - j] = eight % 2
        eight //= 2
    res += tmp


print(int("".join(map(str, res))))