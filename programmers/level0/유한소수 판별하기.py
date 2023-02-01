def solution(a, b):
  answer = 0
  gcd = 1

  for i in range(2, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
      gcd = i

  b //= gcd

  while b % 2 == 0:
    b //= 2

  while b % 5 == 0:
    b //= 5

  return 1 if b == 1 else 2
