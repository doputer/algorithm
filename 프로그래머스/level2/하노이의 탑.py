def move(start, end, stack):
  stack.append([start, end])


def hanoi(n, start, end, sub, stack):
  if n == 1:
    move(start, end, stack)
    return

  hanoi(n - 1, start, sub, end, stack)
  move(start, end, stack)
  hanoi(n - 1, sub, end, start, stack)


def solution(n):
  stack = []

  hanoi(n, 1, 3, 2, stack)

  return stack
