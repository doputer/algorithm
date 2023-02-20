from collections import deque


def bfs(x, y, place):
  queue = deque([(x, y, 0)])
  visit = [[0] * 5 for _ in range(5)]

  while queue:
    x, y, move = queue.popleft()

    visit[y][x] = 1

    if 0 < move <= 2 and place[y][x] == 'P':
      return False
    elif move > 2:
      continue

    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
      nx, ny = x + dx, y + dy

      if 0 <= nx < 5 and 0 <= ny < 5 and not visit[ny][nx]:
        if place[ny][nx] != 'X':
          queue.append((nx, ny, move + 1))

  return True


def solution(places):
  answer = []

  for place in places:
    place = list(map(lambda x: list(x), place))

    safe = True

    for i in range(5):
      for j in range(5):
        if place[i][j] == 'P' and not bfs(j, i, place):
          safe = False
          break
      if not safe:
        break

    answer.append(1 if safe else 0)

  return answer
