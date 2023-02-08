def solution(n):
  change = {0: '4', 1: '1', 2: '2'}
  number = ''

  while n > 0:
    m, mod = divmod(n, 3)

    number += change[mod]

    if n % 3 == 0:
      m -= 1

    n = m

  return number[::-1]
