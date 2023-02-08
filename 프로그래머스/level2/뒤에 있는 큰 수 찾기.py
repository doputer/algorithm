def solution(numbers):
  answer = [-1] * len(numbers)
  stack = [(0, numbers[0])]

  for i in range(1, len(numbers)):
    while stack and stack[-1][1] < numbers[i]:
      index, _ = stack.pop()
      answer[index] = numbers[i]

    stack.append((i, numbers[i]))

  return answer
