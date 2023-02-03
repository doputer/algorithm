def dfs(i, n, computers):
  global visited

  stack = [i]

  while stack:
    i = stack.pop()

    visited[i] = True

    for j in range(n):
      if not visited[j] and computers[i][j]:
        stack.append(j)


def solution(n, computers):
  global visited

  count = 0
  visited = [False] * n

  for i in range(n):
    if not visited[i]:
      dfs(i, n, computers)
      count += 1

  return count
