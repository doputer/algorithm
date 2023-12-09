from collections import deque


def dfs(vertex, graph, visited):
    print(vertex, end=" ")

    visited[vertex - 1] = 1

    for i in graph[vertex]:
        if not visited[i - 1]:
            dfs(i, graph, visited)


def bfs(vertex, graph, visited):
    queue = deque([vertex])

    while queue:
        v = queue.popleft()

        print(v, end=" ")

        visited[v - 1] = 1

        for i in graph[v]:
            if not visited[i - 1] and i not in queue:
                queue.append(i)


graph = {}

n, m, vertex = map(int, input().split())

graph[vertex] = []

for _ in range(m):
    v, e = map(int, input().split())

    if v in graph:
        graph[v].append(e)
    else:
        graph[v] = [e]

    if e in graph:
        graph[e].append(v)
    else:
        graph[e] = [v]

for value in graph.values():
    value.sort()

visited = [0] * n

dfs(vertex, graph, visited)

print()

visited = [0] * n

bfs(vertex, graph, visited)
