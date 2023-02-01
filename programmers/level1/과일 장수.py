def solution(k, m, score):
  score = sorted(score, reverse=True)

  return sum(min(score[i: i + m]) * m for i in range(0, len(score) - len(score) % m, m))
