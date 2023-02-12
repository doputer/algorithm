def dfs(pos, board):
  x, y = pos

  if x >= len(board) or y >= len(board):
    return 0

  move = board[y][x]

  if move == -1:
    return 1
  elif move == 0:
    return 0

  ans = 0

  ans += dfs((x + move, y), board)
  ans += dfs((x, y + move), board)

  return ans


n = int(input())

board = []

for _ in range(n):
  board.append(list(map(int, input().split())))

ans = dfs((0, 0), board)

print('HaruHaru') if ans else print('Hing')
