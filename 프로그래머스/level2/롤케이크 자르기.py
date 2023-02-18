def solution(topping):
  left = set()
  right = {}
  count = 0

  for t in topping:
    if t in right:
      right[t] += 1
    else:
      right[t] = 1

  for t in topping:
    left.add(t)
    right[t] -= 1

    if right[t] == 0:
      del(right[t])

    if len(left) == len(right.keys()):
      count += 1

  return count
