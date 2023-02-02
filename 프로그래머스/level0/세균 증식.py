def solution(n, t):
  return sum(n * 2 ** i for i in range(t)) + n
