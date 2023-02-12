def dfs(i, computers):
  computers[i][i] = 1

  for j in range(len(computers)):
    if not computers[j][j] and computers[i][j]:
      dfs(j, computers)


n = int(input())
m = int(input())

computers = [[0] * n for _ in range(n)]

for _ in range(m):
  i, j = map(int, input().split())

  computers[i - 1][j - 1] = 1
  computers[j - 1][i - 1] = 1

dfs(0, computers)

print(sum(computers[i][i] for i in range(1, n)))
