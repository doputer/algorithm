def solution(numbers):
  answer = []

  for number in numbers:
    if number % 2 == 0:
      answer.append(number + 1)
    else:
      b = list(bin(number)[2::])

      if '0' not in b:
        b[0] = '0'
        b = ['1'] + b
      else:
        for i in range(len(b) - 2, -1, -1):
          if b[i] == '0':
            b[i] = '1'
            b[i + 1] = '0'
            break

      answer.append(int(''.join(b), 2))

  return answer
