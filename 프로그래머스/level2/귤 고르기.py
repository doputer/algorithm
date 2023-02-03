def solution(k, tangerine):
  count = {}

  for i in tangerine:
    if i in count:
      count[i] += 1
    else:
      count[i] = 1

  pick = 0

  for i in sorted(count.values(), reverse=True):
    k -= i
    pick += 1

    if k <= 0:
      break

  return pick
