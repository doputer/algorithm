def hasSequence(l, target):
  count = 0

  for i in l:
    if i >= target:
      count += 1
    else:
      count = 0

    if count == target:
      return True

  return False


def solution(board):
  maximum = 0
  l = [0] * len(board[0])

  for row in board:
    for i in range(len(row)):
      if row[i] == 0:
        l[i] = 0
      else:
        l[i] += 1

    if hasSequence(l, maximum + 1):
      maximum += 1

  return maximum ** 2
