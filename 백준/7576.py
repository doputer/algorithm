from collections import deque

m, n = map(int, input().split())

tomato = []

for _ in range(n):
  tomato.append(list(map(int, input().split())))

queue = deque()
visit = [[0] * m for _ in range(n)]

for i in range(n):
  for j in range(m):
    if tomato[i][j] == 1:
      queue.append((j, i))
      visit[i][j] = 1

day = 0

while queue:
  x, y = queue.popleft()

  for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
    nx, ny = x + dx, y + dy

    if 0 <= nx < m and 0 <= ny < n:
      if tomato[ny][nx] != -1 and not visit[ny][nx]:
        queue.append((nx, ny))
        visit[ny][nx] = visit[y][x] + 1
        day = max(visit[ny][nx], day)

isRipe = True

for i in range(n):
  for j in range(m):
    if tomato[i][j] == 0 and visit[i][j] == 0:
      print(-1)
      isRipe = False
      break
  if not isRipe:
    break

if isRipe:
  print(day - 1 if day > 0 else 0)
