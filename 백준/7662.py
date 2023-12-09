import sys
from heapq import heappush, heappop


t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())

    max_heap = []
    min_heap = []
    count = {}

    for _ in range(k):
        o, n = sys.stdin.readline().split()

        if o == "I":
            heappush(max_heap, -int(n))
            heappush(min_heap, int(n))

            if int(n) in count:
                count[int(n)] += 1
            else:
                count[int(n)] = 1
        elif int(n) > 0:
            while max_heap:
                item = -heappop(max_heap)

                if count[item] > 0:
                    count[item] -= 1
                    break
        else:
            while min_heap:
                item = heappop(min_heap)

                if count[item] > 0:
                    count[item] -= 1
                    break

    if sum(count.values()) > 0:
        count = dict(filter(lambda x: x[1] > 0, count.items()))
        maximum, minimum = max(count.keys()), min(count.keys())

        print(maximum, minimum)
    else:
        print("EMPTY")
