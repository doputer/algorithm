def solution(board, h, w):
    ans = 0
    size = len(board)

    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if 0 <= w + dx < size and 0 <= h + dy < size and board[h + dy][w + dx] == board[h][w]:
            ans += 1

    return ans
