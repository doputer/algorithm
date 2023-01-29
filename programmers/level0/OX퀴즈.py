def solution(quiz):
  answer = []

  for i in quiz:
    q = i.split(' ')

    if q[1] == '+':
      answer.append(int(q[0]) + int(q[2]) == int(q[4]))
    else:
      answer.append(int(q[0]) - int(q[2]) == int(q[4]))

  return ['O' if i else 'X' for i in answer]
