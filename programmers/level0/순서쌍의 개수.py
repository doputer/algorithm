def solution(n):
  count = sum(1 for i in range(1, int(n ** 0.5) + 1) if n % i == 0) * 2

  return count - 1 if n ** 0.5 % 1 == 0 else count
