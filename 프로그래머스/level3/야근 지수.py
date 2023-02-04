from heapq import heapify, heappush, heappop


def solution(n, works):
  if n >= sum(works):
    return 0

  works = [-work for work in works]
  heapify(works)

  while n > 0:
    heappush(works, heappop(works) + 1)
    n -= 1

  return sum(i ** 2 for i in works)
