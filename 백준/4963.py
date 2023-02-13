import sys

sys.setrecursionlimit(10**6)


def dfs(pos, board, visited):
  x, y = pos

  visited[y][x] = 1

  for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
      if not dx and not dy:
        continue

      nx, ny = x + dx, y + dy

      if 0 <= nx < len(board[0]) and 0 <= ny < len(board):
        if board[ny][nx] and not visited[ny][nx]:
          dfs((nx, ny), board, visited)


ans = []

while True:
  w, h = map(int, input().split())

  if w == 0 and h == 0:
    break

  board = []

  for _ in range(h):
    board.append(list(map(int, input().split())))

  visited = [[0] * w for _ in range(h)]
  count = 0

  for i in range(h):
    for j in range(w):
      if board[i][j] and not visited[i][j]:
        dfs((j, i), board, visited)
        count += 1

  ans.append(count)

print(*ans, sep="\n")
