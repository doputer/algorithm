def solution(n, t, m, p):
  answer = '0'
  number = 0
  dic = {str(i - 55): chr(i) for i in range(65, 71)}

  while True:
    temp = number
    next = []

    while temp > 0:
      if str(temp % n) in dic:
        next.append(dic[str(temp % n)])
      else:
        next.append(str(temp % n))
      temp //= n

    answer += ''.join(reversed(next))

    if len(answer) > t * m + p:
      break

    number += 1

  print(answer)

  return ''.join([answer[i - 1] for i in range(p, t * m + p, m)])
