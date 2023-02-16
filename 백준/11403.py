n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  for j in range(n):
    if matrix[i][j] == 0:
      matrix[i][j] = float('inf')

for k in range(n):
  for i in range(n):
    for j in range(n):
      matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

for i in range(n):
  for j in range(n):
    if matrix[i][j] == float('inf'):
      matrix[i][j] = 0
    else:
      matrix[i][j] = 1

  print(*matrix[i])
