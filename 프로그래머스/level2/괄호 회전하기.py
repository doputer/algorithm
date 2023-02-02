from collections import deque


def check(string):
  stack = []

  for i in string:
    if stack:
      if i == ')' and stack[-1] == '(':
        stack.pop()
        continue
      elif i == '}' and stack[-1] == '{':
        stack.pop()
        continue
      elif i == ']' and stack[-1] == '[':
        stack.pop()
        continue

    stack.append(i)

  return not stack


def solution(s):
  answer = 0
  queue = deque(s)

  for i in range(len(queue)):
    if check(''.join(queue)) == True:
      answer += 1

    queue.rotate(-1)

  return answer
