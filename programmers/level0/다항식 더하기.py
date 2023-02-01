def solution(polynomial):
  answer = ''
  a, b = 0, 0

  for i in polynomial.split(' + '):
    if 'x' in i:
      if 'x' == i:
        a += 1
      else:
        a += int(i.replace('x', ''))
    else:
      b += int(i)

  if a:
    if a == 1:
      answer += 'x'
    else:
      answer += str(a) + 'x'

    if b:
      answer += ' + '
  if b:
    answer += str(b)

  return answer
