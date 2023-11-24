from collections import deque


def solution(land):
    oil = [0] * len(land[0])
    visited = set()

    for i in range(len(land)):
        for j in range(len(land[0])):
            sub_oil = 0
            queue = deque()
            visited_x = set()

            if land[i][j] == 1 and (j, i) not in visited:
                queue.append((j, i))
                visited.add((j, i))

                while queue:
                    x, y = queue.popleft()
                    sub_oil += 1
                    visited_x.add(x)

                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if 0 <= x + dx < len(land[0]) and 0 <= y + dy < len(land):
                            if land[y + dy][x + dx] == 1 and (x + dx, y + dy) not in visited:
                                queue.append((x + dx, y + dy))
                                visited.add((x + dx, y + dy))

            for k in visited_x:
                oil[k] += sub_oil

    return max(oil)
