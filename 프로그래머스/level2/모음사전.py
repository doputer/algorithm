def solution(word):
  order = 1

  l = ['A', 'E', 'I', 'O', 'U', '']
  stack = ['A']

  while ''.join(stack) != word:
    order += 1

    if len(stack) < 5:
      stack += 'A'
    else:
      last = stack.pop()
      last = l[l.index(last) + 1]

      if last != '':
        stack.append(last)
      else:
        while stack[-1] == 'U':
          stack.pop()

        last = stack.pop()
        last = l[l.index(last) + 1]
        stack.append(last)

  return order
