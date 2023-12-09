from collections import deque

n = int(input())
grid = [list(input()) for _ in range(n)]

queue = deque()
visited = set()
cnt1 = 0

for i in range(n):
    for j in range(n):
        if (i, j) not in visited:
            cnt1 += 1

            queue.append((i, j))
            visited.add((i, j))
            rgb = grid[i][j]

            while queue:
                y, x = queue.popleft()

                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if 0 <= x + dx < n and 0 <= y + dy < n:
                        if (y + dy, x + dx) not in visited:
                            if grid[y + dy][x + dx] == rgb:
                                queue.append((y + dy, x + dx))
                                visited.add((y + dy, x + dx))

queue = deque()
visited = set()
cnt2 = 0

for i in range(n):
    for j in range(n):
        if (i, j) not in visited:
            cnt2 += 1

            queue.append((i, j))
            visited.add((i, j))

            if grid[i][j] == "B":
                rgb = ["B"]
            else:
                rgb = ["R", "G"]

            while queue:
                y, x = queue.popleft()

                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    if 0 <= x + dx < n and 0 <= y + dy < n:
                        if (y + dy, x + dx) not in visited:
                            if grid[y + dy][x + dx] in rgb:
                                queue.append((y + dy, x + dx))
                                visited.add((y + dy, x + dx))

print(cnt1, cnt2)
