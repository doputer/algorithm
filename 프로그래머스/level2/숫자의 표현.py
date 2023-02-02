def getSum(a, b):
  return (a + b) * (b - a + 1) / 2


def solution(n):
  answer = 0

  for i in range(1, n + 1):
    if i > n // 2 and i != n:
      continue

    for j in range(i, n + 1):
      total = getSum(i, j)

      if total == n:
        answer += 1
        break
      elif total > n:
        break

  return answer
