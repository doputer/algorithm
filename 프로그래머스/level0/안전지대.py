def solution(board):
  safe = set()
  line = len(board)

  for i in range(line):
    for j in range(line):
      if board[i][j] == 1:
        for y in range(max(0, i - 1), min(line, i + 2)):
          for x in range(max(0, j - 1), min(line, j + 2)):
            safe.add((y, x))

  return line ** 2 - len(safe)
