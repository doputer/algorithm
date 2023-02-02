def solution(order):
  l = list(str(order))

  return l.count('3') + l.count('6') + l.count('9')
