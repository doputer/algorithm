from collections import deque


def solution(queue1, queue2):
  queue1 = deque(queue1)
  queue2 = deque(queue2)

  sum1 = sum(queue1)
  sum2 = sum(queue2)

  count = 0

  while sum1 != sum2 and count <= len(queue1) + len(queue2) + 2:
    if sum1 > sum2:
      sum1 -= queue1[0]
      sum2 += queue1[0]

      queue2.append(queue1.popleft())
    else:
      sum1 += queue2[0]
      sum2 -= queue2[0]

      queue1.append(queue2.popleft())

    count += 1

  return count if count <= len(queue1) + len(queue2) + 2 else -1
