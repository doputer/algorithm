def solution():
  n = int(input())

  stair = []

  for _ in range(n):
    stair.append(int(input()))

  score = [0] * n
  score[0] = stair[0]

  if n == 1:
    return score[0]

  score[1] = stair[1] + stair[0]

  if n == 2:
    return score[1]

  score[2] = max(stair[2] + stair[0], stair[2] + stair[1])

  if n == 3:
    return score[2]

  for i in range(3, n):
    a = stair[i] + stair[i - 1] + score[i - 3]
    b = stair[i] + score[i - 2]

    score[i] = max(a, b)

  return score[-1]


print(solution())
