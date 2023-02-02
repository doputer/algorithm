def solution(n):
  return sum([i if i % 2 == 0 else 0 for i in range(2, n + 1)])
