def solution(triangle):
  prev = [triangle[0][0]]
  curr = []

  for i in range(1, len(triangle)):
    for j in range(i + 1):
      if j == 0:
        curr.append(prev[0] + triangle[i][j])
      elif i == j:
        curr.append(prev[j - 1] + triangle[i][j])
      else:
        curr.append(max(prev[j - 1], prev[j]) + triangle[i][j])

    prev = curr
    curr = []

  answer = max(prev)

  return answer
