def solution(keyinput, board):
  pos = [0, 0]
  move = {
      "left": [-1, 0],
      "right": [1, 0],
      "up": [0, 1],
      "down": [0, -1]
  }

  for i in keyinput:
    next = [i + j for i, j in zip(move[i], pos)]

    if abs(next[0]) > (board[0] - 1) // 2 or abs(next[1]) > (board[1] - 1) // 2:
      continue

    pos = next

  return pos
