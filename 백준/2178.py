from sys import setrecursionlimit
from collections import deque

setrecursionlimit(10**6)

n, m = map(int, input().split())

board = []

for _ in range(n):
  board.append(list(map(int, input())))

visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

queue = deque([(0, 0)])

while queue:
  x, y = queue.popleft()

  for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
    nx, ny = x + dx, y + dy

    if 0 <= nx < m and 0 <= ny < n:
      if board[ny][nx] and not visited[ny][nx]:
        visited[ny][nx] = visited[y][x] + 1
        queue.append((nx, ny))

print(visited[-1][-1])
