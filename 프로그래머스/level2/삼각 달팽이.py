from itertools import chain


def solution(n):
  snail = [[0] * i for i in range(1, n + 1)]
  rotate = {'D': 'R', 'R': 'U', 'U': 'D'}
  move = {'D': [0, 1], 'R': [1, 0], 'U': [-1, -1]}

  x, y = 0, 0
  k = 1
  dir = 'D'

  while k <= n * (n + 1) // 2:
    snail[y][x] = k
    k += 1

    dx, dy = move[dir]
    nx, ny = x + dx, y + dy
    isEnd = False

    if dir == 'D' and ny >= n:
      isEnd = True
    elif dir == 'U' and ny < 0:
      isEnd = True
    elif dir == 'R' and nx >= len(snail[ny]):
      isEnd = True
    elif snail[ny][nx]:
      isEnd = True

    if isEnd:
      dir = rotate[dir]
      dx, dy = move[dir]
      nx, ny = x + dx, y + dy

    x, y = nx, ny

  return list(chain(*snail))
