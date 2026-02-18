from collections import deque

N = int(input())

Q = deque()

for i in range(1, N + 1):
    Q.append(i)

odd = 1

while len(Q) > 1:
    if odd % 2 == 1:
        Q.popleft()
    else:
        Q.append(Q.popleft())
    
    odd = 1 - odd

print(Q[0])