def solution(num, k):
  l = list(str(num))

  if str(k) in l:
    return l.index(str(k)) + 1

  return -1
