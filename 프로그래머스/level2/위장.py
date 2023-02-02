def solution(clothes):
  hash = {}

  for _, kind in clothes:
    if kind in hash:
      hash[kind] += 1
    else:
      hash[kind] = 1

  answer = 1

  for i in list(hash.values()):
    answer *= i + 1

  return answer - 1
