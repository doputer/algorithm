def solution(n):
  k = 0

  while n > 1:
    if n % 2 == 1:
      n -= 1
      k += 1
    else:
      n //= 2

  return k + 1
