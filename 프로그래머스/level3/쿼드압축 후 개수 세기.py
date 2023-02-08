def zip(array, offset, length):
  y, x = offset

  for i in range(y, y + length):
    for j in range(x, x + length):
      if array[i][j] != array[y][x]:
        return -1

  return array[y][x]


def solution(arr):
  zero, one = 0, 0
  stack = [((0, 0), len(arr))]

  while stack:
    offset, length = stack.pop()
    res = zip(arr, offset, length)

    if res == -1:
      y, x = offset

      for i in range(y, y + length, length // 2):
        for j in range(x, x + length, length // 2):
          stack.append(((i, j), length // 2))
    else:
      if res == 0:
        zero += 1
      else:
        one += 1

  return [zero, one]
