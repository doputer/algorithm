def solution(dots):
  a, b, c, d = dots
  a, b = list(zip(a, b, c, d))

  return (max(a) - min(a)) * (max(b) - min(b))
