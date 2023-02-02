def solution(survey, choices):
  a = ['R', 'C', 'J', 'A']
  b = ['T', 'F', 'M', 'N']
  score = {i: 0 for i in a + b}

  for i in range(len(survey)):
    score[survey[i][0] if choices[i] < 4 else survey[i][1]] += abs(4 - choices[i])

  type = ''

  for i in range(4):
    if score[b[i]] > score[a[i]]:
      type += b[i]
    else:
      type += a[i]

  return type
