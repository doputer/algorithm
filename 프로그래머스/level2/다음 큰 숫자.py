def getCount(n):
  return str(bin(n))[2:].count('1')


def solution(n):
  answer = 0

  nCount = getCount(n)
  i = 1

  while nCount != getCount(n + i):
    i += 1

  answer = n + i

  return answer
