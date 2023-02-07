def solution(word):
  order = 1

  table = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U'}
  stack = ['A']

  while stack != list(word):
    order += 1

    if len(stack) < 5:
      stack.append('A')
    else:
      while stack[-1] == 'U':
        stack.pop()

      stack.append(table[stack.pop()])

  return order
