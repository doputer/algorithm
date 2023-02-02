def solution(array, n):
  l = [abs(i - n) for i in sorted(array)]

  return sorted(array)[l.index(min(l))]
