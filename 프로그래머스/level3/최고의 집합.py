def solution(n, s):
  if n > s:
    return [-1]

  a, b = divmod(s, n)

  return [a] * (n - b) + [a + 1] * b
