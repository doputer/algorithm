from collections import deque


def bfs(queue, visit, maps, flag):
  while queue:
    x, y = queue.popleft()

    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
      nx, ny = x + dx, y + dy

      if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps):
        if maps[ny][nx] != 'X' and not visit[ny][nx]:
          queue.append((nx, ny))
          visit[ny][nx] = visit[y][x] + 1

          if (nx, ny) == flag:
            return visit[ny][nx]

  return 0


def solution(maps):
  for i in range(len(maps)):
    for j in range(len(maps[i])):
      if maps[i][j] == 'S':
        S = (j, i)
      elif maps[i][j] == 'E':
        E = (j, i)
      elif maps[i][j] == 'L':
        L = (j, i)

  move = 0
  queue = deque([S])
  visit = [[0] * len(maps[0]) for _ in range(len(maps))]

  res = bfs(queue, visit, maps, L)

  if not res:
    return -1

  move += res

  queue = deque([L])
  visit = [[0] * len(maps[0]) for _ in range(len(maps))]

  res = bfs(queue, visit, maps, E)

  if not res:
    return -1

  move += res

  return move
