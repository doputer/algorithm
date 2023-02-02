def solution(n):
  answer = []
  m = 2

  while n // m > 0:
    if n % m == 0:
      answer.append(m)
      n //= m
    else:
      m += 1

  return sorted(list(set(answer)))
