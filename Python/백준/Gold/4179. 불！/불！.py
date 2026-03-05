from sys import stdin
from collections import deque

R, C = map(int, input().split())

Map = [list(i) for i in stdin.read().splitlines()]

Q = deque()

offsets = [ [-1, 0], [1, 0], [0, -1], [0, 1] ]

def printMap(Map):
    for i in Map:
        print(i)
    print()

def solve(Map):
    jNum = 0
    for i in range(R):
        for j in range(C):
            if Map[i][j] == 'J':
                Q.append(('J', i, j, 0))
                Map[i][j] = '.'
                jNum += 1
    for i in range(R):
        for j in range(C):
            if Map[i][j] == 'F':
                Q.append(('F', i, j, 0))
                Map[i][j] = '.'

    while jNum and Q:
        # printMap(Map)
        pt, pi, pj, time = Q.popleft()
        if pt == 'J':
            jNum -= 1
            for offset in offsets:
                di, dj = map(int, offset)
                if 0 <= pi + di < R and 0 <= pj + dj < C:
                    if Map[pi + di][pj + dj] == 'F':
                        Map[pi][pj] = 'F'
                        Q.append(('F', pi, pj, time + 1))
                        break
            if Map[pi][pj] != '.':
                continue
            Map[pi][pj] = 'J'
        else:
            if Map[pi][pj] in ('#', 'F'):
                continue
            Map[pi][pj] = pt
        Map[pi][pj] = pt

        for offset in offsets:
            di, dj = map(int, offset)
            if 0 <= pi + di < R and 0 <= pj + dj < C:
                if Map[pi + di][pj + dj] in ('.', 'J'):
                    Q.append((pt, pi + di, pj + dj, time + 1))
                    if pt == 'J':
                        jNum += 1
            elif pt == 'J':
                return time + 1
    return 'IMPOSSIBLE'

print(solve(Map))
# printMap(Map)