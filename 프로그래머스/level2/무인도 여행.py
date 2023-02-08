from collections import deque


def solution(maps):
  stay = []
  visited = [[0] * len(maps[0]) for _ in range(len(maps))]

  for i in range(len(maps)):
    for j in range(len(maps[i])):
      if not visited[i][j] and maps[i][j] != 'X':
        food = 0
        queue = deque([(i, j)])
        visited[i][j] = 1

        while queue:
          y, x = queue.popleft()

          food += int(maps[y][x])

          for nx, ny in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if 0 <= x + nx < len(maps[i]) and 0 <= y + ny < len(maps):
              if not visited[y + ny][x + nx] and maps[y + ny][x + nx] != 'X':
                queue.append((y + ny, x + nx))
                visited[y + ny][x + nx] = 1

        stay.append(food)

  return [-1] if len(stay) == 0 else sorted(stay)
