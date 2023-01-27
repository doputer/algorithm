def check(board, x, y, dx, dy):
  count = 0

  for i in range(19):
    if x + dx * i < 0 or x + dx * i > 18:
      return count
    if y + dy * i < 0 or y + dy * i > 18:
      return count

    if board[y][x] != board[y + dy * i][x + dx * i]:
      return count

    count += 1


board = [[0 for col in range(19)] for row in range(19)]

N = int(input())

flag = False

for i in range(N):
  y, x = map(int, input().split())
  x -= 1
  y -= 1

  if i % 2 == 0:
    board[y][x] = 1
  else:
    board[y][x] = 2

  # 가로
  count1 = check(board, x, y, 1, 0)
  count2 = check(board, x, y, -1, 0)
  if count1 + count2 - 1 == 5:
    flag = True
    print(i + 1)
    break

  # 세로
  count1 = check(board, x, y, 0, 1)
  count2 = check(board, x, y, 0, -1)
  if count1 + count2 - 1 == 5:
    flag = True
    print(i + 1)
    break

  # 대각
  count1 = check(board, x, y, -1, 1)
  count2 = check(board, x, y, 1, -1)
  if count1 + count2 - 1 == 5:
    flag = True
    print(i + 1)
    break

  # 대각
  count1 = check(board, x, y, 1, 1)
  count2 = check(board, x, y, -1, -1)
  if count1 + count2 - 1 == 5:
    flag = True
    print(i + 1)
    break

if flag != True:
  print(-1)
