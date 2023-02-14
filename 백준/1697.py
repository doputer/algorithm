from collections import deque

n, k = map(int, input().split())

queue = deque([(n, 0)])
visit = [0] * (int(1e5) + 1)

while queue:
  x, t = queue.popleft()

  visit[x] = 1

  if x == k:
    print(t)
    break
  elif x - 1 == k or x + 1 == k or x * 2 == k:
    print(t + 1)
    break

  for nx in [x - 1, x + 1, x * 2]:
    if 0 <= nx <= int(1e5) and not visit[nx]:
      queue.append((nx, t + 1))
