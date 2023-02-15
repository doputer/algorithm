from collections import deque


n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}
visit = [0] * (n + 1)

for _ in range(m):
  u, v = map(int, input().split())

  graph[u].append(v)
  graph[v].append(u)

count = 0

for i in range(1, n + 1):
  if not visit[i]:
    count += 1
    queue = deque([i])

    while queue:
      j = queue.popleft()

      visit[j] = 1

      for k in graph[j]:
        if not visit[k] and k not in queue:
          queue.append(k)

print(count)
