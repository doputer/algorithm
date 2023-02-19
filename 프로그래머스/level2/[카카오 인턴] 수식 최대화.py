def calc(a, b, o):
  if o == '+':
    return a + b
  elif o == '-':
    return a - b
  else:
    return a * b


def solution(expression):
  maximum = 0

  for rank in ['*+-', '*-+', '+*-', '+-*', '-*+', '-+*']:
    operator = []
    operand = []
    n = 0

    for i in expression:
      if i.isdigit():
        n = n * 10 + int(i)
      else:
        operand.append(n)

        while operator and rank.index(operator[-1]) <= rank.index(i):
          b = operand.pop()
          a = operand.pop()
          o = operator.pop()

          operand.append(calc(a, b, o))

        operator.append(i)

        n = 0

    if len(operator) > 1 and rank.index(operator[-1]) < rank.index(operator[-2]):
      a = operand.pop()
      o = operator.pop()

      operand.append(calc(a, n, o))
    else:
      operand.append(n)

    while operator:
      b = operand.pop()
      a = operand.pop()
      o = operator.pop()

      operand.append(calc(a, b, o))

    maximum = max(abs(operand[0]), maximum)

  return maximum
