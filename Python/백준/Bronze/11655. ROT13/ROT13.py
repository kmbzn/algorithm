import sys

S = sys.stdin.readline().strip('\n')

for i in S:
    if 'A' <= i <= 'Z':
        print(chr((ord(i) - ord('A') + 13) % 26 + ord('A')), end = '')
    elif 'a' <= i <= 'z':
        print(chr((ord(i) - ord('a') + 13) % 26 + ord('a')), end = '')
    elif '0' <= i <= '9' or i == ' ':
        print(i, end = '')