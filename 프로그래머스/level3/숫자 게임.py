def solution(A, B):
  A.sort()
  B.sort()

  score = 0

  while A and B:
    if A[-1] < B[-1]:
      score += 1
      A.pop()
      B.pop()
    else:
      A.pop()

  return score
