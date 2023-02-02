def solution(n):
  gcd = 1

  for i in range(2, min(n, 6) + 1):
    if n % i == 0 and 6 % i == 0:
      gcd = i

  return n // gcd
