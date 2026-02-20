# 2149.py

key = list(input())

keySize = len(key)

S = input()

sSize = len(S)

matrix = []

matSize = sSize // keySize

for _ in range(matSize):
    matrix.append([])

for i in range(len(S)):
    matrix[i % matSize].append(S[i])

sortedKey = sorted(key)

decrypt = []

for i in range(keySize):
    for j in range(keySize):
        if key[i] == sortedKey[j]:
            sortedKey[j] = '_'
            decrypt.append(j)
            break

        
for i in range(len(S)):
    print(matrix[i // keySize][decrypt[i % keySize]], end = '')