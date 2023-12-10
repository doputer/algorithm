from collections import deque
from itertools import combinations

n, m = map(int, input().split(" "))
d = ((-1, 0), (1, 0), (0, -1), (0, 1))
init_empty = []
init_virus = []
init_visit = []

empty_count = 0

for i in range(n):
    row = input().split(" ")

    for j, col in enumerate(row):
        if col == "0":
            init_empty.append((i, j))
            empty_count += 1
        elif col == "2":
            init_virus.append((i, j))
            init_visit.append((i, j))

safe_count = 0

for walls in combinations(init_empty, 3):
    queue = deque(init_virus)
    visited = set(init_visit)

    virus = [i for i in init_virus]
    empty = [i for i in init_empty if (i[0], i[1]) not in walls]

    count = empty_count - 3

    while queue:
        i, j = queue.popleft()

        for dx, dy in d:
            if 0 <= i + dy < n and 0 <= j + dx < m:
                if (i + dy, j + dx) not in visited:
                    if (i + dy, j + dx) in empty:
                        virus.append((i + dy, j + dx))
                        queue.append((i + dy, j + dx))
                        visited.add((i + dy, j + dx))
                        count -= 1

    safe_count = max(safe_count, count)

print(safe_count)
