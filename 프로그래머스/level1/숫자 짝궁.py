def solution(X, Y):
  inter = list(set(X) & set(Y))

  if len(inter) == 0:
    return '-1'

  if len(inter) == 1 and inter[0] == '0':
    return '0'

  return ''.join([i * min(X.count(i), Y.count(i)) for i in sorted(inter, reverse=True)])
