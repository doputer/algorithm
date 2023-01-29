def solution(slice, n):
  a, b = divmod(n, slice)

  return a + (1 if b > 0 else 0)
