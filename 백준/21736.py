from collections import deque

n, m = list(map(int, input().split(" ")))

campus = []
start = ()

for i in range(n):
    row = list(input())
    campus.append(row)

    if not start:
        for j, col in enumerate(row):
            if col == "I":
                start = (i, j)

queue = deque([start])
visited = set([start])
meet = 0

while queue:
    i, j = queue.popleft()

    if campus[i][j] == "P":
        meet += 1

    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        if 0 <= i + dy < n and 0 <= j + dx < m:
            if (i + dy, j + dx) not in visited:
                if campus[i + dy][j + dx] in ("O", "P"):
                    queue.append((i + dy, j + dx))
                    visited.add((i + dy, j + dx))

print(meet if meet else "TT")
