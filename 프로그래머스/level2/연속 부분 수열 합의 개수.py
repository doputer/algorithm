def solution(elements):
  answer = set()
  elements *= 2

  for i in range(1, len(elements) // 2 + 1):
    for j in range(0, len(elements) - (len(elements) // 2 - i) - 1):
      answer.add(sum(elements[j: j + i]))

  return len(answer)
