def dfs(curr, prev, board, eat=0, move=3):
  x, y = curr

  if not 0 <= x <= 4 or not 0 <= y <= 4:
    return 0

  if board[y][x] == 1:
    eat += 1

    if eat > 1:
      return 1

  if board[y][x] == -1 or move == 0:
    return 0

  ans = 0

  px, py = prev

  for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
    dx, dy = d
    nx, ny = x + dx, y + dy

    if nx != px or ny != py:
      ans += dfs((nx, ny), (x, y), board, eat, move - 1)

  return ans


board = []

for _ in range(5):
  board.append(list(map(int, input().split())))

r, c = map(int, input().split())

ans = dfs((c, r), (c, r), board)

if ans > 0:
  print(1)
else:
  print(0)
