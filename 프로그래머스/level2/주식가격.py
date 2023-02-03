def solution(prices):
  stack = []
  time = [0] * len(prices)

  for i, j in enumerate(prices):
    if not stack or stack[-1][1] <= j:
      stack.append([i, j])
    else:
      while stack and stack[-1][1] > j:
        a, b = stack.pop()
        time[a] = i - a
      stack.append([i, j])

  while stack:
    a, b = stack.pop()
    time[a] = len(prices) - 1 - a

  return time
