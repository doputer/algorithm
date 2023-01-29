def solution(n):
  numbers = set(range(2, n + 1))
  m = int(n ** 0.5)

  for i in range(2, m + 1):
    if i in numbers:
      numbers -= set(range(i * i, n + 1, i))

  answer = len(numbers)

  return answer
