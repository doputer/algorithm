paper = {-1: 0, 0: 0, 1: 0}


def count(left, right, top, bottom, board):
    point = board[top][left]

    for i in range(top, bottom):
        for j in range(left, right):
            if board[i][j] != point:
                return 2

    paper[point] += 1


def cut(left, right, top, bottom, n, board):
    if n == 1:
        paper[board[top][left]] += 1
        return

    check = count(left, right, top, bottom, board)

    if check == 2:
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                l = left + j * (n // 3)
                r = right - (2 - j) * (n // 3)
                t = top + i * (n // 3)
                b = bottom - (2 - i) * (n // 3)

                cut(l, r, t, b, n // 3, board)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

cut(0, n, 0, n, n, board)

print(*paper.values(), sep="\n")
