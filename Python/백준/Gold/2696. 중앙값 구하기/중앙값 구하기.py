import heapq, math

T = int(input())

printL = 0
def print10(item):
    global printL
    print(item, end = ' ')
    printL += 1
    if printL % 10 == 0:
        print()
        printL = 0


for _ in range(T):
    N = int(input())
    maxHeap = []
    minHeap = []
    I = []
    for _ in range(N // 10 + int(bool(N % 10))):
        I += list(map(int, input().split()))
    print((N + 1) // 2)
    median = I[0]
    print10(median)
    for i in range(1, N, 2):
        a, b = I[i], I[i + 1]
        if a > b:
            a, b = b, a
        if median <= a:
            heapq.heappush(minHeap, a)
            heapq.heappush(minHeap, b)
            heapq.heappush(maxHeap, -median)
            median = heapq.heappop(minHeap)
        elif b <= median:
            heapq.heappush(maxHeap, -a)
            heapq.heappush(maxHeap, -b)
            heapq.heappush(minHeap, median)
            median = -heapq.heappop(maxHeap)
        else:
            heapq.heappush(maxHeap, -a)
            heapq.heappush(minHeap, b)
        print10(median)
    printL = 0
    print()
        