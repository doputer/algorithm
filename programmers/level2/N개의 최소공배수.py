def getGCD(a, b):
  gcd = 1

  for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
      gcd = i

  return gcd


def solution(arr):
  answer = 1

  for i in arr:
    answer = i * answer // getGCD(i, answer)

  return answer
