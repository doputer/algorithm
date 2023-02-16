import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())

heap = []
count = {}

for _ in range(n):
  x = int(sys.stdin.readline())

  if x:
    heappush(heap, abs(x))

    if x < 0:
      if -x in count:
        count[-x] += 1
      else:
        count[-x] = 1
  else:
    if not heap:
      print(0)
      continue

    x = heappop(heap)

    if x in count and count[x] > 0:
      count[x] -= 1
      print(-x)
    else:
      print(x)
