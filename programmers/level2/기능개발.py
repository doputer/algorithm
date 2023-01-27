def solution(progresses, speeds):
  answer = []
  index = 0
  length = len(progresses)

  while index != length:
    for i in range(length):
      progresses[i] += speeds[i]

    count = 0
    for i in range(index, length):
      if progresses[i] >= 100:
        count += 1
      else:
        break

    if count:
      answer.append(count)
      index += count

  return answer
