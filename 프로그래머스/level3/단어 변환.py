from collections import deque


def possible(a, b):
  count = 0

  for i in range(len(a)):
    if a[i] != b[i]:
      count += 1

    if count > 1:
      return False

  return True


def bfs(begin, target, words):
  visited = [0] * len(words)

  queue = deque()

  for i in range(len(words)):
    if not visited[i] and possible(begin, words[i]):
      queue.append(i)
      visited[i] = 1

  while queue:
    prev = queue.popleft()

    if words[prev] == target:
      return visited[words.index(target)]

    for i in range(len(words)):
      if not visited[i] and possible(words[prev], words[i]):
        queue.append(i)
        visited[i] = visited[prev] + 1

  return 0


def solution(begin, target, words):
  return bfs(begin, target, words)
