def solution(s):
  answer = 0
  last = 0

  for i in s.split(' '):
    if i == 'Z':
      answer -= last
    else:
      answer += int(i)
      last = int(i)

  return answer
