import sys

sys.setrecursionlimit(100000)


def dfs(i, j, h):
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = j + dx, i + dy

        if 0 <= nx < n and 0 <= ny < n:
            if (ny, nx) not in visit and graph[ny][nx] > h:
                visit.add((ny, nx))
                dfs(ny, nx, h)


n = int(input())
graph = []
max_height = 0

for _ in range(n):
    row = list(map(int, input().split(" ")))
    graph.append(row)
    max_height = max(row)

ans = 0

for h in range(max_height):
    visit = set()
    safe = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and (i, j) not in visit:
                visit.add((i, j))
                dfs(i, j, h)
                safe += 1

    ans = max(ans, safe)

print(ans)
