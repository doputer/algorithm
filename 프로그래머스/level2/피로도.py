from itertools import permutations


def isPossible(k, routes, dungeons):
  for i in range(len(routes)):
    a, b = dungeons[routes[i]]

    if k < a:
      return i
    else:
      k -= b

  return i + 1


def solution(k, dungeons):
  count = 0

  for routes in permutations(range(len(dungeons)), len(dungeons)):
    count = max(count, isPossible(k, routes, dungeons))

  return count
