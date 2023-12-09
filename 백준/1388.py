n, m = map(int, input().split())

count = 0
tiles = []
visited = [[0] * m for _ in range(n)]

for _ in range(n):
    tiles.append(list(input()))

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = 1
            count += 1

            if tiles[i][j] == "-":
                k = j + 1

                while k < m and tiles[i][k] == "-":
                    visited[i][k] = 1
                    k += 1
            else:
                k = i + 1

                while k < n and tiles[k][j] == "|":
                    visited[k][j] = 1
                    k += 1

print(count)
