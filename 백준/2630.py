import sys


colors = {0: 0, 1: 0}


def check(left, right, top, bottom, board):
  color = board[top][left]

  for i in range(top, bottom):
    for j in range(left, right):
      if board[i][j] != color:
        return -1

  return color


def divide(left, right, top, bottom, board):
  color = check(left, right, top, bottom, board)

  if color == 0 or color == 1:
    colors[color] += 1
    return
  elif right - left == 1 and bottom - top == 1:
    colors[board[top][left]] += 1
    return

  hm = (left + right) // 2
  vm = (top + bottom) // 2

  divide(left, hm, top, vm, board)
  divide(hm, right, top, vm, board)
  divide(left, hm, vm, bottom, board)
  divide(hm, right, vm, bottom, board)


n = int(sys.stdin.readline())

board = []

for _ in range(n):
  board.append(list(map(int, sys.stdin.readline().split())))

divide(0, n, 0, n, board)

print(colors[0])
print(colors[1])
