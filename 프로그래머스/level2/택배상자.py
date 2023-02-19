from collections import deque


def solution(order):
  queue = deque(list(range(1, len(order)+1)))
  stack = []

  target = 0

  while queue or stack:
    if queue and queue[0] == order[target]:
      queue.popleft()
      target += 1
    elif stack and stack[-1] == order[target]:
      stack.pop()
      target += 1
    else:
      stack.append(queue.popleft())

    if queue and queue[0] > order[target] and stack and stack[-1] > order[target]:
      break

  return target
