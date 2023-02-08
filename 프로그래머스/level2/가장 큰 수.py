def solution(numbers):
  l = []

  for number in numbers:
    s = str(number) * 4
    l.append(((str(number) * 4)[:4], len(str(number))))

  l.sort(reverse=True)

  answer = ''.join(list(map(lambda x: x[0][:x[1]], l)))

  return '0' if int(answer) == 0 else answer
