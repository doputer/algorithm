def check(left, right, top, bottom, board):
  point = board[top][left]

  for i in range(top, bottom):
    for j in range(left, right):
      if board[i][j] != point:
        return -1

  return point


def compress(left, right, top, bottom, board):
  if right - left == 1 and bottom - top == 1:
    return board[top][left]

  z = check(left, right, top, bottom, board)

  if z != -1:
    return z

  tree = []

  hm = (left + right) // 2
  vm = (top + bottom) // 2

  tree += [compress(left, hm, top, vm, board)]
  tree += [compress(hm, right, top, vm, board)]
  tree += [compress(left, hm, vm, bottom, board)]
  tree += [compress(hm, right, vm, bottom, board)]

  return tree


n = int(input())

board = [list(map(int, list(input()))) for _ in range(n)]

compression = str(compress(0, n, 0, n, board))

print(compression.replace('[', '(').replace(']', ')').replace(', ', ''))
