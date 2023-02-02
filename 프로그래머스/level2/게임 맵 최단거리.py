def bfs(maps, curr, queue):
  visited = [[0] * len(maps[0]) for _ in maps]
  visited[0][0] = 1

  queue.append(curr)

  while len(queue) > 0:
    x, y = queue.pop(0)

    for dx in [-1, 1]:
      if 0 <= x + dx < len(maps[0]) and maps[y][x + dx]:
        if not visited[y][x + dx]:
          queue.append((x + dx, y))
          visited[y][x + dx] = visited[y][x] + 1

    for dy in [-1, 1]:
      if 0 <= y + dy < len(maps) and maps[y + dy][x]:
        if not visited[y + dy][x]:
          queue.append((x, y + dy))
          visited[y + dy][x] = visited[y][x] + 1

  return -1 if visited[-1][-1] == 0 else visited[-1][-1]


def solution(maps):
  return bfs(maps, (0, 0), [])
