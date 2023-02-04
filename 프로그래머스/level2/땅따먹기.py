def solution(land):
  for i in range(1, len(land)):
    for j in range(4):
      maximum = 0
      for k in range(4):
        if j != k:
          maximum = max(maximum, land[i - 1][k])
      land[i][j] += maximum

  return max(land[-1])
