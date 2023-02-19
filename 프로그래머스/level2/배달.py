# Dijkstra
def findNode(graph, visit):
  weight = float('inf')
  node = -1

  for i in range(len(graph)):
    if weight > graph[i] and not visit[i]:
      weight = graph[i]
      node = i

  return node


def solution(N, road, K):
  maps = [[0] * N for _ in range(N)]

  for r in road:
    a, b, c = r

    if maps[a-1][b-1] > c or not maps[a-1][b-1]:
      maps[a-1][b-1] = c
      maps[b-1][a-1] = c

  graph = [0] + [float('inf')] * (N-1)
  visit = [0] * N

  for _ in range(N - 1):
    node = findNode(graph, visit)
    visit[node] = 1

    for i in range(N):
      if maps[node][i] and graph[i] > graph[node] + maps[node][i] and not visit[i]:
        graph[i] = graph[node] + maps[node][i]

  return sum(1 for i in graph if i <= K)


# Floyd-Warshall
def solution(N, road, K):
  graph = [[0] * N for _ in range(N)]

  for r in road:
    a, b, c = r

    if not graph[a-1][b-1] or graph[a-1][b-1] > c:
      graph[a-1][b-1] = c
      graph[b-1][a-1] = c

  for i in range(N):
    for j in range(N):
      if i != j and graph[i][j] == 0:
        graph[i][j] = float('inf')

  for k in range(N):
    for i in range(N):
      for j in range(N):
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

  return sum(1 for i in graph[0] if i <= K)
