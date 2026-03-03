import heapq
from sys import stdin

N = int(stdin.readline())

plusHeap = []

minusHeap = []

size = 0

L = list(map(int, stdin.read().splitlines()))


for i in L:
    if i == 0:
        if len(plusHeap) == 0:
            if len(minusHeap) > 0:
                print(-heapq.heappop(minusHeap))
            else:
                print(0)
        elif len(minusHeap) == 0:
            print(heapq.heappop(plusHeap))
        elif plusHeap[0] >= minusHeap[0]:
            print(-heapq.heappop(minusHeap))
        else:
            print(heapq.heappop(plusHeap))
    elif i > 0:
        heapq.heappush(plusHeap, i)
    else:
        heapq.heappush(minusHeap, -i)
                