from collections import deque


def solution(board):
    queue = deque()
    visited = set()

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == "R":
                queue.append([i, j, 0])
                visited.add((i, j))

    def move(x, y, dx, dy):
        while 0 <= x + dx < len(board[0]) and 0 <= y + dy < len(board) and board[y + dy][x + dx] != "D":
            x += dx
            y += dy

        return [x, y]

    while queue:
        i, j, k = queue.popleft()
        visited.add((i, j))

        if board[i][j] == "G":
            return k

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y = move(j, i, dx, dy)

            if (y, x) not in visited:
                queue.append([y, x, k + 1])

    return -1
