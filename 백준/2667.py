from collections import deque

n = int(input())

board = []
visit = [[0] * n for _ in range(n)]

for _ in range(n):
    board.append(list(map(int, input())))

count = []

for i in range(n):
    for j in range(n):
        if board[i][j] and not visit[i][j]:
            queue = deque([(j, i)])
            move = 0

            while queue:
                x, y = queue.popleft()

                visit[y][x] = 1
                move += 1

                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in queue:
                        if board[ny][nx] and not visit[ny][nx]:
                            queue.append((nx, ny))

            count.append(move)

count.sort()

print(len(count))
print(*count, sep="\n")
