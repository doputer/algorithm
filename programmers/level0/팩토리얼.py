def fac(n):
  if n == 1 or n == 0:
    return 1

  return n * fac(n - 1)


def solution(n):
  answer = 0

  for i in range(1, n + 1):
    f = fac(i)

    if f > n:
      break

    answer = i

  return answer
