from collections import deque


def findStart(array):
    for i, row in enumerate(array):
        for j, col in enumerate(row):
            if col == 2:
                return [i, j]


n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
maps = [[0] * m for _ in range(n)]

i, j = findStart(array)
length = 0
queue = deque([[i, j, length]])
visited = set([(i, j)])

while queue:
    i, j, length = queue.popleft()
    maps[i][j] = length

    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if 0 <= i + dy < n and 0 <= j + dx < m:
            if array[i + dy][j + dx] == 1:
                if (i + dy, j + dx) not in visited:
                    queue.append([i + dy, j + dx, length + 1])
                    visited.add((i + dy, j + dx))

for i in range(n):
    for j in range(m):
        if (i, j) not in visited and array[i][j] == 1:
            maps[i][j] = -1

for i in maps:
    print(*i)
