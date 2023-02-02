def solution(k, score):
  answer = []
  honor = []

  for i in range(len(score)):
    honor.append(score[i])
    honor.sort()
    honor = honor[-1:-k-1:-1]

    answer.append(min(honor))

  return answer
