def flip(w):
  if w == '':
    return ''

  table = {'(': ')', ')': '('}

  for i in range(len(w)):
    w[i] = table[w[i]]

  return ''.join(w)


def correct(w):
  stack = []

  for i in w:
    if i == '(':
      stack.append(True)
    else:
      if len(stack) == 0:
        return False

      stack.pop()

  return True if len(stack) == 0 else False


def balance(w):
  open, close = 0, 0

  for i in range(len(w)):
    if w[i] == '(':
      open += 1
    else:
      close += 1

    if open == close:
      break

  return [''.join(w[:i+1]), ''.join(w[i+1:])]


def change(w):
  if w == '':
    return ''

  u, v = balance(w)

  if correct(u):
    return u + change(v)

  s = '('
  s += change(v)
  s += ')'

  return s + flip(list(u[1:-1]))


def solution(p):
  return change(p)
