import heapq, sys

T = int(sys.stdin.readline())

res = ""

for _ in range(T):
    maxHeap = []
    minHeap = []

    k = int(sys.stdin.readline())

    Set = set()

    for i in range(k):
        c, v = sys.stdin.readline().split()
        v = int(v)
        if c == 'I':
            heapq.heappush(maxHeap, [-v, i])
            heapq.heappush(minHeap, [v, i])
        else:
            if v > 0:
                while True:
                    if len(maxHeap):
                        popped = heapq.heappop(maxHeap)[1]
                        if popped not in Set:
                            Set.add(popped)
                            break
                    else:
                        break
            else:
                while True:
                    if len(minHeap):
                        popped = heapq.heappop(minHeap)[1]
                        if popped not in Set:
                            Set.add(popped)
                            break
                    else:
                        break

    while True:
        if len(maxHeap):
            popped = heapq.heappop(maxHeap)
            if popped[1] not in Set:
                res += str(-popped[0]) + " "
                while True:
                    if len(minHeap):
                        popped = heapq.heappop(minHeap)
                        if popped[1] not in Set:
                            res += str(popped[0]) + "\n"
                            break
                    else:
                        break
                break
        else:
            res += "EMPTY\n"
            break

print(res)