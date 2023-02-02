def solution(number, limit, power):
  answer = 0

  for i in range(1, number + 1):
    length = len([j for j in range(1, int(i ** 0.5) + 1) if i % j == 0]) * 2

    if i ** 0.5 % 1 == 0:
      length -= 1

    if length <= limit:
      answer += length
    else:
      answer += power

  return answer
