def solution(emergency):
  answer = []
  d = {}

  for i, j in enumerate(sorted(emergency, reverse=True)):
    d[j] = i + 1

  return [d[i] for i in emergency]
