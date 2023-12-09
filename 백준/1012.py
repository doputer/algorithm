import sys

sys.setrecursionlimit(10**6)


def dfs(curr, board, visited):
    x, y = curr

    visited[y][x] = 1

    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(board[0]) and 0 <= ny < len(board):
            if board[ny][nx] and not visited[ny][nx]:
                dfs((nx, ny), board, visited)


t = int(input())
ans = []

for _ in range(t):
    m, n, k = map(int, input().split())

    board = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    count = 0

    for i in range(n):
        for j in range(m):
            if board[i][j] and not visited[i][j]:
                count += 1

                dfs((j, i), board, visited)

    ans.append(count)

print(*ans, sep="\n")
