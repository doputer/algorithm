from itertools import combinations


def solution(number):
  answer = 0

  groups = list(combinations(number, 3))

  for group in groups:
    if sum(group) == 0:
      answer += 1

  return answer
