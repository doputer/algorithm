def solution(m, n, puddles):
  routes = [[0] * m for i in range(n)]

  for i in range(1, m):
    if [i + 1, 1] in puddles:
      break

    routes[0][i] = 1

  for i in range(1, n):
    if [1, i + 1] in puddles:
      break

    routes[i][0] = 1

  for i in range(1, n):
    for j in range(1, m):
      if [j + 1, i + 1] in puddles:
        continue

      routes[i][j] = routes[i - 1][j] + routes[i][j - 1]

  return routes[-1][-1] % 1000000007
