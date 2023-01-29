def solution(n):
  n += 1

  l = [True] * n
  m = int(n ** 0.5)

  for i in range(2, m + 1):
    if l[i]:
      for j in range(i + i, n, i):
        l[j] = False

  return l[2:].count(False)
